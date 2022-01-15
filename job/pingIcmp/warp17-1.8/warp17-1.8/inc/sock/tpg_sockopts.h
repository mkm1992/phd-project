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
 *     tpg_sockopts.h
 *
 * Description:
 *     Holds all types of socket options.
 *
 * Author:
 *     Dumitru Ceara, Eelco Chaudron
 *
 * Initial Created:
 *     06/30/2014
 *
 * Notes:
 *
 */

/*****************************************************************************
 * Multiple include protection
 ****************************************************************************/
#ifndef _H_TPG_SOCKOPTS_
#define _H_TPG_SOCKOPTS_

/*****************************************************************************
 * Definitions
 ****************************************************************************/
typedef struct tcp_sockopt_s {

    uint32_t tcpo_win_size;

    uint8_t  tcpo_syn_retry_cnt;
    uint8_t  tcpo_syn_ack_retry_cnt;
    uint8_t  tcpo_data_retry_cnt;
    uint8_t  tcpo_retry_cnt;

    /* Timeouts in us */
    uint32_t tcpo_rto;
    uint32_t tcpo_fin_to;
    uint32_t tcpo_twait_to;
    uint32_t tcpo_orphan_to;

    /* Flags */
    uint32_t tcpo_skip_timewait : 1;
    uint32_t tcpo_ack_delay : 1;

} tcp_sockopt_t;

typedef struct udp_sockopt_s {

} udp_sockopt_t;

typedef struct ipv4_sockopt_s {

    uint32_t ip4so_rx_tstamp : 1;
    uint32_t ip4so_tx_tstamp : 1;

    uint8_t  ip4so_tos;
    uint8_t  ip4so_hdr_opt_len; /* Len of "ipv4_option_hdr_t" needed in order
                                 * to calculate MTU.
                                 */
} ipv4_sockopt_t;

typedef struct ipv6_sockopt_s {

} ipv6_sockopt_t;

typedef struct eth_sockopt_s {

    /* Flags */
    uint8_t ethso_tx_offload_ipv4_cksum : 1;
    uint8_t ethso_tx_offload_tcp_cksum  : 1;
    uint8_t ethso_tx_offload_udp_cksum  : 1;

} eth_sockopt_t;

typedef struct vlan_sockopt_s {

    uint16_t vlanso_id;
    uint8_t  vlanso_pri;
    uint8_t  vlanso_hdr_opt_len; /* Len of vlan header; needed in order
                                  * to provide VLAN info in the packet or NOT.
                                  */
} vlan_sockopt_t;

typedef struct sockopt_s {

    /* L1 options. */
    union {
        eth_sockopt_t so_eth;
    };

    /* L2 options. */
    union {
        vlan_sockopt_t so_vlan;
    };

    /* L3 options. */
    union {
        ipv4_sockopt_t so_ipv4;
        ipv6_sockopt_t so_ipv6;
    };

    /* L4 options. */
    union {
        tcp_sockopt_t so_tcp;
        udp_sockopt_t so_udp;
    };

} sockopt_t;

/*****************************************************************************
 * Globals
 ****************************************************************************/

/*****************************************************************************
 * Static inlines
 ****************************************************************************/

/*****************************************************************************
 * ipv4_get_sockopt()
 ****************************************************************************/
static inline const ipv4_sockopt_t *ipv4_get_sockopt(const sockopt_t *opts)
{
    return &opts->so_ipv4;
}

/*****************************************************************************
 * ipv6_get_sockopt()
 ****************************************************************************/
static inline const ipv6_sockopt_t *ipv6_get_sockopt(const sockopt_t *opts)
{
    return &opts->so_ipv6;
}

/*****************************************************************************
 * vlan_get_sockopt()
 ****************************************************************************/
static inline const vlan_sockopt_t *vlan_get_sockopt(const sockopt_t *opts)
{
    return &opts->so_vlan;
}

/*****************************************************************************
 * tcp_get_sockopt()
 ****************************************************************************/
static inline const tcp_sockopt_t *tcp_get_sockopt(const sockopt_t *opts)
{
    return &opts->so_tcp;
}

/*****************************************************************************
 * udp_get_sockopt()
 ****************************************************************************/
static inline const udp_sockopt_t *udp_get_sockopt(const sockopt_t *opts)
{
    return &opts->so_udp;
}

/*****************************************************************************
 * End of include file
 ****************************************************************************/
#endif /* _H_TPG_SOCKOPTS_ */


