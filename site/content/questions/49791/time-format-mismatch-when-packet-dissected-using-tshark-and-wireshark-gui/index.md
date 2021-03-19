+++
type = "question"
title = "Time format mismatch when packet dissected using tshark and Wireshark GUI"
description = '''Hi all I have a PCAP containing a message with fields of type UTC timestamp (7-bytes in length - YYYYDDMMHHMMSS format). When Wireshark dissect this message it properly displays the timestamp like ex: 19991212121212. Where as when dissected using tshark (used to export to CSV files) it diplays like ...'''
date = "2016-02-03T11:03:00Z"
lastmod = "2016-03-30T08:11:00Z"
weight = 49791
keywords = [ "timestamp", "csv" ]
aliases = [ "/questions/49791" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Time format mismatch when packet dissected using tshark and Wireshark GUI](/questions/49791/time-format-mismatch-when-packet-dissected-using-tshark-and-wireshark-gui)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49791-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49791-score" class="post-score" title="current number of votes">0</div><span id="post-49791-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all</p><p>I have a PCAP containing a message with fields of type UTC timestamp (7-bytes in length - YYYYDDMMHHMMSS format). When Wireshark dissect this message it properly displays the timestamp like ex: 19991212121212. Where as when dissected using tshark (used to export to CSV files) it diplays like "Jun 20, 107456758 10:19:19.1386439036 IST". I am not sure what is the reason behind this. I also observed that if i use tshark to just dissect (without using options to export to CSV files) then the format looks fine.</p><p>I went through the man page for tshark and found that there is a option "-t" to specify the timestamp in the summary lines, i tried all the option but still observed same. Can anyone please let me know if i am missing something. I basically want both Wireshark GUI and tshark (used to export to CSV files) to display the same time format (UTC - 7-bytes in length - YYYYDDMMHHMMSS).</p><p>tshark command used to export fields to CSV files is as below. /usr/bin/tshark -T fields -E separator=, -E header=y -E aggregator=~ -E quote=d -e &lt;list of="" fields=""&gt; -n -r &lt;filename&gt; &gt; /tmp/details.csv</p><p>Thank you</p><p>Kiran Kumar G</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timestamp" rel="tag" title="see questions tagged &#39;timestamp&#39;">timestamp</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Feb '16, 11:03</strong></p><img src="https://secure.gravatar.com/avatar/ae4b5aebc9d00c273018cc64d3ac583a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kiran%20Kumar%20G&#39;s gravatar image" /><p><span>Kiran Kumar G</span><br />
<span class="score" title="21 reputation points">21</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kiran Kumar G has no accepted answers">0%</span></p></div></div><div id="comments-container-49791" class="comments-container"><span id="49826"></span><div id="comment-49826" class="comment"><div id="post-49826-score" class="comment-score"></div><div class="comment-text"><p>Can you share a Pcap (Google Drive, Dropbox etc.) containing the frame with the data in question?</p></div><div id="comment-49826-info" class="comment-info"><span class="comment-age">(04 Feb '16, 07:46)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="51232"></span><div id="comment-51232" class="comment"><div id="post-51232-score" class="comment-score"></div><div class="comment-text"><p>Hi Graham</p><p>Sorry for the delay in reply.</p><p>The message to be dissected and having issue is dissected using my custom plugin. If i share the pcap file will you be able to dissect it ?. Can you please let me know if any other info i can share with you for analysis ? (picture, dissection snapshot etc).</p><p>Regards Kiran Kumar G</p></div><div id="comment-51232-info" class="comment-info"><span class="comment-age">(28 Mar '16, 07:13)</span> <span class="comment-user userinfo">Kiran Kumar G</span></div></div><span id="51233"></span><div id="comment-51233" class="comment"><div id="post-51233-score" class="comment-score"></div><div class="comment-text"><p>Without the plugin as well we won't be able to see the results of the dissection.</p><p>As it's a custom plugin, can you share the code, or if not, the fragment that reads the data from the field and adds it to the dissection results.</p></div><div id="comment-51233-info" class="comment-info"><span class="comment-age">(28 Mar '16, 07:23)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="51288"></span><div id="comment-51288" class="comment"><div id="post-51288-score" class="comment-score"></div><div class="comment-text"><p>Hi Graham</p><p>I am providing the requirement with the code snippet used to get this done. Also, i am providing the output and the issue observed.</p><p>Requirement: Need to export dissected output of a message into CSV file (all fields of a message). Problem Statement: Some of fields of these messages are 7 bytes UTC timestamp (7-bytes in length - YYYYDDMMHHMMSS format). When Wireshark dissect this message it properly displays the timestamp like ex: 19991212121212. Where as when dissected using tshark (used to export to CSV files) it diplays like "Jun 20, 107456758 10:19:19.1386439036 IST".</p><p>Code snippet: Following is the code which is used to extract the 7 bytes and display in UTC time format.</p><p><code> struct utc_time  {         guint16 year;         guint8 month;   guint8 day;   guint8 hour;   guint8 minute;   guint8 seconds; };</code></p><p><code></code></p><p><code>void gd_dissect_UTC_time_data (tvbuff_t tvb, int offset, struct utc_time utc_time)</code></p><code></code><p>{</p><p>utc_time-&gt;year = tvb_get_ntohs(tvb, offset);.</p><p>utc_time-&gt;month = tvb_get_guint8(tvb,offset+2);</p><p>utc_time-&gt;day = tvb_get_guint8(tvb,offset+3);</p><p>utc_time-&gt;hour = tvb_get_guint8(tvb,offset+4);</p><p>utc_time-&gt;minute = tvb_get_guint8(tvb,offset+5);</p><p>utc_time-&gt;seconds = tvb_get_guint8(tvb,offset+6);</p><p>}</p><p>===========================================================</p><p>dissect_UTC_time_data (tvb, <em>tvb_offset, &amp;utc_time_data); proto_tree_add_time_format_value (gd_msg_tree,</em> (temp_icd_proto_info_ptr-&gt;proto_hf_ptr[temp_msg_field_details_ptr-&gt;field_hf_ref_index].p_id), tvb, <em>tvb_offset, temp_field_size, (nstime_t</em> ) &amp;utc_time_data, "%d%02d%02d%02d%02d%02d", utc_time_data.year, utc_time_data.month, utc_time_data.day, utc_time_data.hour, utc_time_data.minute, utc_time_data.seconds ); ===========================================================</p></code><p><code></code></p><p>Output: Displayed on Wireshark GUI. 1999121212121212 (YYYYDDMMHHMMSS)</p><p>Displayed when exported to CSV using tshark command. Feb 2, 590961086 22:29:56.1250822016 IST</p><p>It should have displayed like 1999121212121212 .. right ?</p><p>Please let me know if any more information is required.</p><p>Thank you. Kiran Kumar G</p></div><div id="comment-51288-info" class="comment-info"><span class="comment-age">(30 Mar '16, 05:54)</span> <span class="comment-user userinfo">Kiran Kumar G</span></div></div></div><div id="comment-tools-49791" class="comment-tools"></div><div class="clear"></div><div id="comment-49791-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51291"></span>

<div id="answer-container-51291" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51291-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51291-score" class="post-score" title="current number of votes">0</div><span id="post-51291-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can't simply cast <code>utc_time_data</code> to <code>nstime_t</code> and expect it to work in the call to <code>proto_tree_add_time_format_value()</code>.</p><p>You'll have to create a variable of type <code>nstime_t</code>, set the members correctly and then pass a pointer to that variable into the call to <code>proto_tree_add_time_format_value()</code>.</p><p>Even having done that, I'm not sure that tshark will print the time formatted as you want, report back what happens.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '16, 08:11</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-51291" class="comments-container"></div><div id="comment-tools-51291" class="comment-tools"></div><div class="clear"></div><div id="comment-51291-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

