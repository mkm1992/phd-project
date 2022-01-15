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
 *     tpg_test_raw_app.c
 *
 * Description:
 *     Holds the application state callbacks. Each application should define
 *     its own callbacks here.
 *
 * Author:
 *     Dumitru Ceara, Eelco Chaudron
 *
 * Initial Created:
 *     02/22/2016
 *
 * Notes:
 *
 */

/*****************************************************************************
 * Include files
 ****************************************************************************/
#include "tcp_generator.h"

/*****************************************************************************
 * Globals
 ****************************************************************************/

DECLARE_APP_CB_ARRAY(app_default_cfg_cb_t, app_default_cfg_handlers) = {
    DEFINE_APP_CB(APP_PROTO__RAW_CLIENT, raw_client_default_cfg),
    DEFINE_APP_CB(APP_PROTO__RAW_SERVER, raw_server_default_cfg),
    DEFINE_APP_CB(APP_PROTO__HTTP_CLIENT, http_client_default_cfg),
    DEFINE_APP_CB(APP_PROTO__HTTP_SERVER, http_server_default_cfg),
    DEFINE_APP_CB(APP_PROTO__IMIX, imix_default_cfg),
};

DECLARE_APP_CB_ARRAY(app_validate_cfg_cb_t, app_validate_cfg_handlers) = {
    DEFINE_APP_CB(APP_PROTO__RAW_CLIENT, raw_client_validate_cfg),
    DEFINE_APP_CB(APP_PROTO__RAW_SERVER, raw_server_validate_cfg),
    DEFINE_APP_CB(APP_PROTO__HTTP_CLIENT, http_client_validate_cfg),
    DEFINE_APP_CB(APP_PROTO__HTTP_SERVER, http_server_validate_cfg),
    DEFINE_APP_CB(APP_PROTO__IMIX, imix_validate_cfg),
};

DECLARE_APP_CB_ARRAY(app_print_cfg_cb_t, app_print_cfg_handlers) = {
    DEFINE_APP_CB(APP_PROTO__RAW_CLIENT, raw_client_print_cfg),
    DEFINE_APP_CB(APP_PROTO__RAW_SERVER, raw_server_print_cfg),
    DEFINE_APP_CB(APP_PROTO__HTTP_CLIENT, http_client_print_cfg),
    DEFINE_APP_CB(APP_PROTO__HTTP_SERVER, http_server_print_cfg),
    DEFINE_APP_CB(APP_PROTO__IMIX, imix_print_cfg),
};

DECLARE_APP_CB_ARRAY(app_add_delete_cfg_cb_t, app_add_cfg_handlers) = {
    DEFINE_APP_CB(APP_PROTO__RAW_CLIENT, raw_add_delete_cfg),
    DEFINE_APP_CB(APP_PROTO__RAW_SERVER, raw_add_delete_cfg),
    DEFINE_APP_CB(APP_PROTO__HTTP_CLIENT, http_client_add_cfg),
    DEFINE_APP_CB(APP_PROTO__HTTP_SERVER, http_server_add_cfg),
    DEFINE_APP_CB(APP_PROTO__IMIX, imix_add_cfg),
};

DECLARE_APP_CB_ARRAY(app_add_delete_cfg_cb_t, app_delete_cfg_handlers) = {
    DEFINE_APP_CB(APP_PROTO__RAW_CLIENT, raw_add_delete_cfg),
    DEFINE_APP_CB(APP_PROTO__RAW_SERVER, raw_add_delete_cfg),
    DEFINE_APP_CB(APP_PROTO__HTTP_CLIENT, http_client_delete_cfg),
    DEFINE_APP_CB(APP_PROTO__HTTP_SERVER, http_server_delete_cfg),
    DEFINE_APP_CB(APP_PROTO__IMIX, imix_delete_cfg),
};

DECLARE_APP_CB_ARRAY(app_pkts_per_send_cb_t, app_pkts_per_send_handlers) = {
    DEFINE_APP_CB(APP_PROTO__RAW_CLIENT, raw_client_pkts_per_send),
    DEFINE_APP_CB(APP_PROTO__RAW_SERVER, raw_server_pkts_per_send),
    DEFINE_APP_CB(APP_PROTO__HTTP_CLIENT, http_client_pkts_per_send),
    DEFINE_APP_CB(APP_PROTO__HTTP_SERVER, http_server_pkts_per_send),
    DEFINE_APP_CB(APP_PROTO__IMIX, imix_pkts_per_send),
};

DECLARE_APP_CB_ARRAY(app_init_cb_t, app_init_handlers) = {
    DEFINE_APP_CB(APP_PROTO__RAW_CLIENT, raw_client_init),
    DEFINE_APP_CB(APP_PROTO__RAW_SERVER, raw_server_init),
    DEFINE_APP_CB(APP_PROTO__HTTP_CLIENT, http_client_server_init),
    DEFINE_APP_CB(APP_PROTO__HTTP_SERVER, http_client_server_init),
    DEFINE_APP_CB(APP_PROTO__IMIX, imix_init_session),
};

DECLARE_APP_CB_ARRAY(app_tc_start_stop_cb_t, app_tc_start_handlers) = {
    DEFINE_APP_CB(APP_PROTO__RAW_CLIENT, raw_client_tc_start),
    DEFINE_APP_CB(APP_PROTO__RAW_SERVER, raw_server_tc_start),
    DEFINE_APP_CB(APP_PROTO__HTTP_CLIENT, http_client_tc_start),
    DEFINE_APP_CB(APP_PROTO__HTTP_SERVER, http_server_tc_start),
    DEFINE_APP_CB(APP_PROTO__IMIX, imix_tc_start),
};

DECLARE_APP_CB_ARRAY(app_tc_start_stop_cb_t, app_tc_stop_handlers) = {
    DEFINE_APP_CB(APP_PROTO__RAW_CLIENT, raw_tc_stop),
    DEFINE_APP_CB(APP_PROTO__RAW_SERVER, raw_tc_stop),
    DEFINE_APP_CB(APP_PROTO__HTTP_CLIENT, http_client_tc_stop),
    DEFINE_APP_CB(APP_PROTO__HTTP_SERVER, http_server_tc_stop),
    DEFINE_APP_CB(APP_PROTO__IMIX, imix_tc_stop),
};

DECLARE_APP_CB_ARRAY(app_conn_up_cb_t, app_conn_up_handlers) = {
    DEFINE_APP_CB(APP_PROTO__RAW_CLIENT, raw_client_conn_up),
    DEFINE_APP_CB(APP_PROTO__RAW_SERVER, raw_server_conn_up),
    DEFINE_APP_CB(APP_PROTO__HTTP_CLIENT, http_client_conn_up),
    DEFINE_APP_CB(APP_PROTO__HTTP_SERVER, http_server_conn_up),
    DEFINE_APP_CB(APP_PROTO__IMIX, imix_conn_up),
};

DECLARE_APP_CB_ARRAY(app_conn_down_cb_t, app_conn_down_handlers) = {
    DEFINE_APP_CB(APP_PROTO__RAW_CLIENT, raw_conn_down),
    DEFINE_APP_CB(APP_PROTO__RAW_SERVER, raw_conn_down),
    DEFINE_APP_CB(APP_PROTO__HTTP_CLIENT, http_client_server_conn_down),
    DEFINE_APP_CB(APP_PROTO__HTTP_SERVER, http_client_server_conn_down),
    DEFINE_APP_CB(APP_PROTO__IMIX, imix_conn_down),
};

DECLARE_APP_CB_ARRAY(app_deliver_cb_t, app_deliver_handlers) = {
    DEFINE_APP_CB(APP_PROTO__RAW_CLIENT, raw_client_deliver_data),
    DEFINE_APP_CB(APP_PROTO__RAW_SERVER, raw_server_deliver_data),
    DEFINE_APP_CB(APP_PROTO__HTTP_CLIENT, http_client_deliver_data),
    DEFINE_APP_CB(APP_PROTO__HTTP_SERVER, http_server_deliver_data),
    DEFINE_APP_CB(APP_PROTO__IMIX, imix_deliver_data),
};

DECLARE_APP_CB_ARRAY(app_send_cb_t, app_send_handlers) = {
    DEFINE_APP_CB(APP_PROTO__RAW_CLIENT, raw_send_data),
    DEFINE_APP_CB(APP_PROTO__RAW_SERVER, raw_send_data),
    DEFINE_APP_CB(APP_PROTO__HTTP_CLIENT, http_client_send_data),
    DEFINE_APP_CB(APP_PROTO__HTTP_SERVER, http_server_send_data),
    DEFINE_APP_CB(APP_PROTO__IMIX, imix_send_data),
};

DECLARE_APP_CB_ARRAY(app_data_sent_cb_t, app_data_sent_handlers) = {
    DEFINE_APP_CB(APP_PROTO__RAW_CLIENT, raw_client_data_sent),
    DEFINE_APP_CB(APP_PROTO__RAW_SERVER, raw_server_data_sent),
    DEFINE_APP_CB(APP_PROTO__HTTP_CLIENT, http_client_data_sent),
    DEFINE_APP_CB(APP_PROTO__HTTP_SERVER, http_server_data_sent),
    DEFINE_APP_CB(APP_PROTO__IMIX, imix_data_sent),
};

DECLARE_APP_CB_ARRAY(app_stats_init_global_cb_t,
                     app_stats_init_global_handlers) = {
    DEFINE_APP_CB(APP_PROTO__RAW_CLIENT, raw_stats_init),
    DEFINE_APP_CB(APP_PROTO__RAW_SERVER, raw_stats_init),
    DEFINE_APP_CB(APP_PROTO__HTTP_CLIENT, http_stats_init),
    DEFINE_APP_CB(APP_PROTO__HTTP_SERVER, http_stats_init),
    DEFINE_APP_CB(APP_PROTO__IMIX, imix_stats_init_global),
};

DECLARE_APP_CB_ARRAY(app_stats_init_req_cb_t, app_stats_init_req_handlers) = {
    DEFINE_APP_CB(APP_PROTO__RAW_CLIENT, raw_stats_init),
    DEFINE_APP_CB(APP_PROTO__RAW_SERVER, raw_stats_init),
    DEFINE_APP_CB(APP_PROTO__HTTP_CLIENT, http_stats_init),
    DEFINE_APP_CB(APP_PROTO__HTTP_SERVER, http_stats_init),
    DEFINE_APP_CB(APP_PROTO__IMIX, imix_stats_init_req),
};

DECLARE_APP_CB_ARRAY(app_stats_init_cb_t, app_stats_init_handlers) = {
    DEFINE_APP_CB(APP_PROTO__RAW_CLIENT, raw_stats_init),
    DEFINE_APP_CB(APP_PROTO__RAW_SERVER, raw_stats_init),
    DEFINE_APP_CB(APP_PROTO__HTTP_CLIENT, http_stats_init),
    DEFINE_APP_CB(APP_PROTO__HTTP_SERVER, http_stats_init),
    DEFINE_APP_CB(APP_PROTO__IMIX, imix_stats_init),
};

DECLARE_APP_CB_ARRAY(app_stats_copy_cb_t, app_stats_copy_handlers) = {
    DEFINE_APP_CB(APP_PROTO__RAW_CLIENT, raw_stats_copy),
    DEFINE_APP_CB(APP_PROTO__RAW_SERVER, raw_stats_copy),
    DEFINE_APP_CB(APP_PROTO__HTTP_CLIENT, http_stats_copy),
    DEFINE_APP_CB(APP_PROTO__HTTP_SERVER, http_stats_copy),
    DEFINE_APP_CB(APP_PROTO__IMIX, imix_stats_copy),
};

DECLARE_APP_CB_ARRAY(app_stats_add_cb_t, app_stats_add_handlers) = {
    DEFINE_APP_CB(APP_PROTO__RAW_CLIENT, raw_stats_add),
    DEFINE_APP_CB(APP_PROTO__RAW_SERVER, raw_stats_add),
    DEFINE_APP_CB(APP_PROTO__HTTP_CLIENT, http_stats_add),
    DEFINE_APP_CB(APP_PROTO__HTTP_SERVER, http_stats_add),
    DEFINE_APP_CB(APP_PROTO__IMIX, imix_stats_add),
};

DECLARE_APP_CB_ARRAY(app_stats_print_cb_t, app_stats_print_handlers) = {
    DEFINE_APP_CB(APP_PROTO__RAW_CLIENT, raw_stats_print),
    DEFINE_APP_CB(APP_PROTO__RAW_SERVER, raw_stats_print),
    DEFINE_APP_CB(APP_PROTO__HTTP_CLIENT, http_stats_print),
    DEFINE_APP_CB(APP_PROTO__HTTP_SERVER, http_stats_print),
    DEFINE_APP_CB(APP_PROTO__IMIX, imix_stats_print),
};

