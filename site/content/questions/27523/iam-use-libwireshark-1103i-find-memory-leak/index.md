+++
type = "question"
title = "i&#x27;am use libwireshark 1.10.3,i find memory leak"
description = '''i&#x27;am use libwireshark 1.10.3,i find memory leak，is it any question with my program XJ_DISSECT_PKT* xj_dissect_packet() { #ifdef XJ_DISSECT_PACKET_LINUX_DEF  if (!g_xj_process_policies_called)  {  init_process_policies();//初始化本地权限  g_xj_process_policies_called = true;  } #endif   if(!g_binitepan)  { ...'''
date = "2013-11-28T01:18:00Z"
lastmod = "2013-11-28T01:18:00Z"
weight = 27523
keywords = [ "libwireshark", "memory", "leak" ]
aliases = [ "/questions/27523" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [i'am use libwireshark 1.10.3,i find memory leak](/questions/27523/iam-use-libwireshark-1103i-find-memory-leak)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27523-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i'am use libwireshark 1.10.3,i find memory leak，is it any question with my program</p><pre><code>XJ_DISSECT_PKT*  xj_dissect_packet()
{
#ifdef XJ_DISSECT_PACKET_LINUX_DEF
    if (!g_xj_process_policies_called)
    {
        init_process_policies();//初始化本地权限
        g_xj_process_policies_called = true;
    }
#endif

    if(!g_binitepan)
    {
        epan_init(register_all_protocols, register_all_protocol_handoffs, 
            NULL, NULL, NULL, NULL, NULL, NULL);

        cleanup_dissection();//clean up environment
        init_dissection();//init dissect environment

        g_binitepan = true;
        //tap_queue_init(&amp;edt);//队列
    }

    frame_data  *fdata;
    epan_dissect_t  *edt;
    wtap_pkthdr  pseudo_header;
    pseudo_header.interface_id = 0;
    pseudo_header.caplen       = 0;
    pseudo_header.len          = -1;
    pseudo_header.pkt_encap    = 1;
    pseudo_header.pack_flags   = 0;
    pseudo_header.drop_count   = 0;
    pseudo_header.opt_comment  = NULL;

    fdata = (frame_data*)g_new(frame_data, 1);

    memset(fdata, 0, sizeof(frame_data));
    fdata-&gt;pfd  = NULL;
    fdata-&gt;num = 1;
    fdata-&gt;interface_id = 0;
    fdata-&gt;pkt_len  = DATA_LEN;
    fdata-&gt;cap_len  = DATA_LEN;
    fdata-&gt;cum_bytes = 0;
    fdata-&gt;file_off = 0;
    fdata-&gt;subnum = 0;
    fdata-&gt;lnk_t = WTAP_ENCAP_ETHERNET;
    fdata-&gt;flags.encoding = PACKET_CHAR_ENC_CHAR_ASCII;
    fdata-&gt;flags.visited = 0;
    fdata-&gt;flags.marked = 0;
    fdata-&gt;flags.ref_time = 0;
    fdata-&gt;color_filter = NULL;
    fdata-&gt;abs_ts.secs = 0;
    fdata-&gt;abs_ts.nsecs = 0;
    fdata-&gt;opt_comment = NULL;

    nstime_t       elapsed_time;    /* Elapsed time */
    nstime_t       first_ts;
    nstime_t       prev_dis_ts;
    nstime_t       prev_cap_ts;
    guint32 cum_bytes = 0;

    nstime_set_zero(&amp;elapsed_time);
    nstime_set_zero(&amp;first_ts);
    nstime_set_zero(&amp;prev_dis_ts);
    nstime_set_zero(&amp;prev_cap_ts);

    edt = epan_dissect_new(TRUE, TRUE);
    //frame_data_set_before_dissect(fdata, &amp;elapsed_time, &amp;first_ts, &amp;prev_dis_ts, &amp;prev_cap_ts);
    epan_dissect_run(edt, &amp;pseudo_header, xjdata, fdata, NULL);

    epan_dissect_free(edt);
    //frame_data_cleanup(fdata);
    frame_data_destroy(fdata);
    g_free(fdata);
    //cleanup_dissection();

    printf(&quot;successful call xj_dissect_packet...\n&quot;);

    return NULL;
}

 void MySleep(UINT nmilliseconds)
{
#ifdef OS_WINDOWS
    //Sleep(nmilliseconds);
#endif

#ifdef OS_LINUX
    timeval tm;
    tm.tv_sec =  nmilliseconds / 1000;
    tm.tv_usec = (nmilliseconds % 1000) * 1000;
    int nret=select(0, 0, 0, 0, &amp;tm);
#endif
}

 int main(int argc, char *argv[])
{
    XJ_DISSECT_PKT* pXjstruct = NULL;

    while (!g_bExit)
    {
        pXjstruct = xj_dissect_packet();
        xj_cleanup_packet(pXjstruct);//释放资源

        MySleep(50);
    }

    if (g_binitepan)
    {
        cleanup_dissection();
        epan_cleanup();
    }

    return 0;
}</code></pre></div><div id="question-tags" class="tags-container tags">libwireshark memory leak</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Nov '13, 01:18</strong></p><img src="https://secure.gravatar.com/avatar/e4c7e91e5da0e1a1573a9d34afcb566a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lipeng5555&#39;s gravatar image" /><p>lipeng5555<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lipeng5555 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Nov '13, 12:22</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-27523" class="comments-container"></div><div id="comment-tools-27523" class="comment-tools"></div><div class="clear"></div><div id="comment-27523-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

