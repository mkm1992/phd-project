/*
 * DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER
 *
 * Copyright (c) 2016, Juniper Networks, Inc. All rights reserved.
 *
 *
 * The contents of this file are subject to the terms of the BSD 3 clause
 * License (the "License"). You may not use this file except in compliance
 * with the License.
 *
 * You can obtain a copy of the license at
 * https://github.com/Juniper/warp17/blob/master/LICENSE.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 * 1. Redistributions of source code must retain the above copyright notice,
 * this list of conditions and the following disclaimer.
 *
 * 2. Redistributions in binary form must reproduce the above copyright
 * notice, this list of conditions and the following disclaimer in the
 * documentation and/or other materials provided with the distribution.
 *
 * 3. Neither the name of the copyright holder nor the names of its
 * contributors may be used to endorse or promote products derived from this
 * software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 *
 * File name:
 *     tpg_cli.h
 *
 * Description:
 *     Command line interface for the warp17 tool.
 *
 * Author:
 *     Dumitru Ceara, Eelco Chaudron
 *
 * Initial Created:
 *     06/05/2015
 *
 * Notes:
 *
 */

/*****************************************************************************
 * Multiple include protection
 ****************************************************************************/
#ifndef _H_TPG_CLI_
#define _H_TPG_CLI_

/*****************************************************************************
 * Definitions
 ****************************************************************************/
#define CLI_CMDLINE_OPTIONS() \
    CMDLINE_OPT_ARG("cmd-file", true)

#define CLI_CMDLINE_PARSER() \
    CMDLINE_ARG_PARSER(cli_handle_cmdline_opt, NULL,                       \
"  --cmd-file=<file>:          CLI command file to be executed when the\n" \
"                              application starts\n")

typedef int (*tpg_cli_override_cb_t)(char *buf, uint32_t size);

/*****************************************************************************
 * Quoted string parser definitions.
 ****************************************************************************/
extern struct cmdline_token_ops cli_token_quoted_string_ops;

#define TOKEN_QUOTED_STRING_INITIALIZER(structure, field) { \
    /* hdr */                                               \
    {                                                       \
        &cli_token_quoted_string_ops, /* ops */             \
        offsetof(structure, field),       /* offset */      \
    },                                                      \
    /* string_data */                                       \
    {                                                       \
        TOKEN_STRING_MULTI,               /* str */         \
    },                                                      \
}

/*****************************************************************************
 * ID List parser definitions.
 ****************************************************************************/

/* WARNING: HACK! We abuse cmdline_parse_token_portlist_t because it's
 * exactly what we need (except for the help string)..
 */
typedef cmdline_portlist_t             cmdline_id_list_t;
typedef cmdline_parse_token_portlist_t cmdline_parse_token_id_list_t;

extern struct cmdline_token_ops cmdline_token_id_list_ops;

#define TOKEN_ID_LIST_INITIALIZER(structure, field)  \
{                                                    \
    /* hdr */                                        \
    {                                                \
        &cmdline_token_id_list_ops,   /* ops */      \
        offsetof(structure, field),   /* offset */   \
    },                                               \
}

/*****************************************************************************
 * Externals for tpg_cli.c
 ****************************************************************************/
extern void cli_printer(void *printer_arg, const char *fmt, va_list ap);

extern bool cli_init(void);
extern void cli_exit(void);
extern bool cli_set_override(tpg_cli_override_cb_t override);
extern bool cli_unset_override(void);
extern void cli_redisplay_prompt(void);
extern bool cli_run_input_file(const char *filename);
extern void cli_interact(void);
extern bool cli_add_main_ctx(cmdline_parse_ctx_t *ctx);
extern int  cli_parse_quoted_string(cmdline_parse_token_hdr_t *tk,
                                    const char *buf,
                                    void *res,
                                    unsigned ressize);
extern int cmdline_get_help_id_list(cmdline_parse_token_hdr_t *tk,
                                    char *dstbuf,
                                    unsigned int size);

extern cmdline_arg_parser_res_t cli_handle_cmdline_opt(const char *opt_name,
                                                       char *opt_arg);

#endif /* _H_TPG_CLI_ */

