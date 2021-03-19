+++
type = "question"
title = "Calling MAC-LTE Dissectors using LUA"
description = '''Hello,  I am trying to call dissector for mac-lte using lua. But getting error &quot;Lua Error: ...logCapture.lua:27: attempt to call field &#x27;get_mac_lte_proto_data&#x27; (a nil value)&quot;. I am passing the buffer as per the framing pattern for heuristic dissector. Here below is the lua script snippet: do  print(...'''
date = "2015-09-27T07:15:00Z"
lastmod = "2015-09-28T07:29:00Z"
weight = 46195
keywords = [ "mac-lte", "lua", "dissector" ]
aliases = [ "/questions/46195" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Calling MAC-LTE Dissectors using LUA](/questions/46195/calling-mac-lte-dissectors-using-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46195-score" class="post-score" title="current number of votes">0</div><span id="post-46195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am trying to call dissector for mac-lte using lua. But getting error "Lua Error: ...logCapture.lua:27: attempt to call field 'get_mac_lte_proto_data' (a nil value)". I am passing the buffer as per the framing pattern for heuristic dissector.</p><p>Here below is the lua script snippet:</p><pre><code>do
   print(&quot;hello Lua!!!&quot;)

   local uelog_proto = Proto(&quot;uelog&quot;,&quot;UE Log Protocol&quot;)

   -- create a function to dissect it
   function uelog_proto.dissector(buffer,pinfo,tree)

      local dissector = Dissector.get(&quot;mac-lte&quot;)
      if dissector ~= nil then
     print(&quot;Buffer %x,%x,%x \n&quot;,buffer(0,1):uint(),buffer(1,1):uint(),buffer(2,1):uint())
         --dissector:call(buffer(0):tvb(),pinfo,tree)
     --pinfo.proto_data=NULL
    print(&quot;Value %s&quot;,buffer(0,7):string())

    --pinfo.cols.info:set(buffer(0,7):string()) 
        --pinfo.cols.protocol = &quot;udp&quot;
     local mac_lte_info = dissector.get_mac_lte_proto_data(pinfo)
     mac_lte_info.radioType = buffer(8,1):uint()
     mac_lte_info.direction = buffer(9,1):uint()
     mac_lte_info.rntiType  = buffer(10,1):uint()
         dissector.set_mac_lte_proto_data(pinfo,mac_lte_info)
         dissector:call(buffer(14):tvb(),pinfo,tree)
      else 
         print(string.format(&quot;dissector not found, pkt number = %d&quot;, pinfo.number ))
      end

    end

   -- load the udp.port table
   udp_table = DissectorTable.get(&quot;udp.port&quot;)
   -- register our protocol to handle udp port 5001
   udp_table:add(5003,uelog_proto)

end</code></pre><p>C code for framing Mac-Lte PDU :</p><pre><code>void SendMACFrame(guint8 radioType, guint8 direction, guint8 rntiType,
                  guint16 rnti, guint16 ueid, guint16 subframeNumber,
                  guint8 isPredefinedData, guint8 retx, guint8 crcStatus,char *macpdu,guint8 length,struct UE_LogHeader *uelog )
{
    ssize_t bytesSent;
    unsigned int  g_frameOffset = 0;    
    unsigned short tmp16;
    char *g_frameBuffer = &amp;uelog-&gt;data[0]; 
    /********************************************************************/
    /* Fixed start to each frame (allowing heuristic dissector to work) */
    /* Not NULL terminated */
    memcpy(g_frameBuffer+g_frameOffset, MAC_LTE_START_STRING,
           strlen(MAC_LTE_START_STRING));
    g_frameOffset += strlen(MAC_LTE_START_STRING);
    TRACE_LOG(&quot;MAC PUD Direction %d ,length %d rntiType %d\n&quot;,direction ,length,rntiType ); 
    /******************************************************************************/
    /* Now write out fixed fields (the mandatory elements of struct mac_lte_info) */
    g_frameBuffer[g_frameOffset++] = radioType;
    g_frameBuffer[g_frameOffset++] = direction;
    g_frameBuffer[g_frameOffset++] = rntiType;

    /*************************************/
    /* Now optional fields               */

/* Subframe number */
    g_frameBuffer[g_frameOffset++] = MAC_LTE_FRAME_SUBFRAME_TAG;
    tmp16 = htons(subframeNumber);
    memcpy(g_frameBuffer+g_frameOffset, &amp;tmp16, 2);
    g_frameOffset += 2;
#if 0
    /* RNTI */
     g_frameBuffer[g_frameOffset++] = MAC_LTE_RNTI_TAG;
    tmp16 = htons(rnti);
    memcpy(g_frameBuffer+g_frameOffset, &amp;tmp16, 2);
    g_frameOffset += 2;

    /* UEId */
    g_frameBuffer[g_frameOffset++] = MAC_LTE_UEID_TAG;
    tmp16 = htons(ueid);
    memcpy(g_frameBuffer+g_frameOffset, &amp;tmp16, 2);
    g_frameOffset += 2;

    /* Subframe number */
    g_frameBuffer[g_frameOffset++] = MAC_LTE_SUBFRAME_TAG;
    tmp16 = htons(ueid);
    memcpy(g_frameBuffer+g_frameOffset, &amp;tmp16, 2);
    g_frameOffset += 2;

    g_frameBuffer[g_frameOffset++] = MAC_LTE_CRC_STATUS_TAG;
    g_frameBuffer[g_frameOffset++] = crcStatus;

    /***********************************************************/
    /* For these optional fields, no need to encode if value is default */
    if (!isPredefinedData) {
        g_frameBuffer[g_frameOffset++] = MAC_LTE_PREDFINED_DATA_TAG;
        g_frameBuffer[g_frameOffset++] = isPredefinedData;
    }

    if (retx != 0) {
        g_frameBuffer[g_frameOffset++] = MAC_LTE_RETX_TAG;
        g_frameBuffer[g_frameOffset++] = retx;
    }

#endif

    /***************************************/
    /* Now write the MAC PDU               */
    g_frameBuffer[g_frameOffset++] = MAC_LTE_PAYLOAD_TAG;

    /* Append actual PDU  */
    memcpy(g_frameBuffer+g_frameOffset, macpdu, length);
    g_frameOffset += length;

   destination.sin_port = htons(5003);   
    /* Send out the data over the UDP socket */
    bytesSent = sendto(rrcSockFd , uelog-&gt;data, g_frameOffset , 
               SEND_FLAG, (struct sockaddr *)&amp;destination, sizeof(destination));

    if (bytesSent != g_frameOffset) {
        fprintf(stderr, &quot;sendto() failed - expected %d bytes, got %d (errno=%d)\n&quot;,
                g_frameOffset, bytesSent, errno);
        exit(1);
    }

}</code></pre><p>Above mentioned C code works fine for wireshark If I disable lua script and simply enable heuristic dissector in wireshark. But I want to call dissector through lua as I have written some addtional dissectors related to generic UE specific information.</p><p>I am new to lua scripting, please help me out .</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mac-lte" rel="tag" title="see questions tagged &#39;mac-lte&#39;">mac-lte</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '15, 07:15</strong></p><img src="https://secure.gravatar.com/avatar/328293431c288f04f47108594a783709?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amittkumm&#39;s gravatar image" /><p><span>amittkumm</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amittkumm has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Sep '15, 10:21</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-46195" class="comments-container"><span id="46217"></span><div id="comment-46217" class="comment"><div id="post-46217-score" class="comment-score"></div><div class="comment-text"><p>Can anybody tell whether is it even possible to call mac-lte heuristic dissectors through lua or should I try it with C code ?</p></div><div id="comment-46217-info" class="comment-info"><span class="comment-age">(28 Sep '15, 04:26)</span> <span class="comment-user userinfo">amittkumm</span></div></div></div><div id="comment-tools-46195" class="comment-tools"></div><div class="clear"></div><div id="comment-46195-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46218"></span>

<div id="answer-container-46218" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46218-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46218-score" class="post-score" title="current number of votes">0</div><span id="post-46218-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is the same thing as what we discussed in your <a href="https://ask.wireshark.org/questions/46050/rlc-lte-heuristic-dissector-issue">previous question</a>.</p><p>If you want to put your dissector between UDP and MAC-LTE, then you need to manually fill the mac_lte_info structure and attach it to pinfo. See dissect_mac_lte_heur() function in packet-mac-lte.c file.</p><p>The call to get_mac_lte_proto_data() will give you a NULL pointer as no one has added the mac_lte_info structure to pinfo yet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '15, 07:29</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-46218" class="comments-container"></div><div id="comment-tools-46218" class="comment-tools"></div><div class="clear"></div><div id="comment-46218-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

