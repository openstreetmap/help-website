+++
type = "question"
title = "How is the time duration field of an SSL session computed?"
description = '''I am trying to figure out how you can tell the time duration of an SSL session. In Wireshark, if you choose from the File Menu Statistics -&amp;gt; Conversations -&amp;gt; TCP -&amp;gt; Limit to filter, you get results based on your filter. If I choose &quot;SSL&quot; as my filter than all the results would be SSL packet...'''
date = "2011-09-14T04:30:00Z"
lastmod = "2011-09-14T05:18:00Z"
weight = 6355
keywords = [ "duration", "ssl", "session", "time" ]
aliases = [ "/questions/6355" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How is the time duration field of an SSL session computed?](/questions/6355/how-is-the-time-duration-field-of-an-ssl-session-computed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6355-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to figure out how you can tell the time duration of an SSL session. In Wireshark, if you choose from the File Menu Statistics -&gt; Conversations -&gt; TCP -&gt; Limit to filter, you get results based on your filter. If I choose "SSL" as my filter than all the results would be SSL packets/sessions. My question is "How is the time duration field of the SSL session computed?" I am having difficulty finding out what keeps track of an SSL session.</p><p>Any help would be greatly appreciated.</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags">duration ssl session time</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '11, 04:30</strong></p><img src="https://secure.gravatar.com/avatar/9afed7ed17019861bc68d7785f8d5c4f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gakar06&#39;s gravatar image" /><p>gakar06<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gakar06 has no accepted answers">0%</span></p></div></div><div id="comments-container-6355" class="comments-container"></div><div id="comment-tools-6355" class="comment-tools"></div><div class="clear"></div><div id="comment-6355-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6356"></span>

<div id="answer-container-6356" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6356-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The "Duration" column in the Conversation statistics is the time difference between the first packet seen in the conversation and the last packet seen in the conversation.</p><p>When you use the option "limit to display filter", the first and last packet seen in a particular conversation can change. As in your case, the filter "ssl" won't match the packets of the 3-way handshake, so the first packet seen in the TCP conversation that is displayed when the filter "ssl" is active, is the ClientHello. The last packet seen will either be a data packet (with unclean shutdown enabled on the server) or an EncryptedAlert message. The FIN packets and the last ACK will not be seen when using the filter "ssl". So the duration column will show the time between the ClientHello and the last data/alert packet.</p><p>If you want to include the TCP session setup and teardown in the calculation of the duration column, you can use the display filter "tcp.port==443" instead of "ssl".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '11, 05:18</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-6356" class="comments-container"><span id="6371"></span><div id="comment-6371" class="comment"><div id="post-6371-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the quick response SYNbit. I will definitely use "tcp.port == 443" instead of "SSL" to make the SSL session duration more accurate but I guess what I am asking is how can you tell what SSL packets are specific to a given SSL session. I know in the Conversation statistics the information is there for you but how did they determine for instance "these 5 packets make up this SSL session". I am wanting to search several packet capture files (or a directory full of files) to pull out/extract the duration of each SSL session but I am not sure how to determine what part of the packet signifies "hey, this is the start of the session". Is there a session identifier that would show if 5 packets are apart of the same SSL session?<br />
</p></div><div id="comment-6371-info" class="comment-info"><span class="comment-age">(14 Sep '11, 13:35)</span> gakar06</div></div><span id="6374"></span><div id="comment-6374" class="comment"><div id="post-6374-score" class="comment-score"></div><div class="comment-text"><p>(converted your "answer" to a "comment", see the FAQ for details)</p><p>In the TCP conversations overview, the IP addresses and TCP ports determine whether a packet belongs to a certain TCP session. Please note that in that window, there is no knowledge about SSL sessions, all is treated as TCP. But each TCP session can only belong to one SSL session, so in practice you are fine (unless you want to combine statistics for reused SSL sessions in which case multiple TCP conversations can belong to the same SSL session).</p></div><div id="comment-6374-info" class="comment-info"><span class="comment-age">(14 Sep '11, 15:18)</span> SYN-bit ♦♦</div></div><span id="6379"></span><div id="comment-6379" class="comment"><div id="post-6379-score" class="comment-score"></div><div class="comment-text"><p>So what I was doing was combining the Src IP, Src Port, Dst IP, and Dst Port together to make basically a "unique key". So I concatenated the 4 fields together and was basically assuming that when these 4 fields are present, it represents a session.<br />
</p><p>For example, all 4 of the fields below (with the specific data in each field present) would represent a session. Does that make sense? Src IP -&gt; 123.123.123.123 Src Port -&gt; 15451 Dst IP -&gt; 213.213.213.213 Dst Port -&gt; 443</p><p>With these results, I was able to determine the time of each session by subtracting the max(time) from the min(time). I did a count of the "unique key" above to give me the total number of sessions per "unique key". The issue I currently see with this is that the output could contain several different sessions because the dates could range from say May through August (and obviously the session didn't last that long).</p><p>So to make a long story short, I was trying to figure out how to determine the length of an SSL session and how I could determine if one packet was part of a "certain" SSL session.</p><p>Any ideas? Does what I described above make sense?</p><p>Gakar06</p></div><div id="comment-6379-info" class="comment-info"><span class="comment-age">(14 Sep '11, 18:30)</span> gakar06</div></div><span id="6382"></span><div id="comment-6382" class="comment"><div id="post-6382-score" class="comment-score"></div><div class="comment-text"><p>(please use "add comment" instead of "Your Answer" when replying, see the FAQ)</p><p>When multiple TCP sessions exist with the same combination of ip-addresses and tcp-ports, then you need to split up the sessions at the TCP SYN packets. That is the marker for a new session. Wireshark does this in the packet list and it will show you "[ports reused]" on the SYN of the new session. It will also assign a new tcp.stream number to all packets (which you can use to differate them too).</p><p>I'm not sure if the output in the conversation statistics takes multiple sessions with the same into account.</p></div><div id="comment-6382-info" class="comment-info"><span class="comment-age">(15 Sep '11, 00:36)</span> SYN-bit ♦♦</div></div><span id="6384"></span><div id="comment-6384" class="comment"><div id="post-6384-score" class="comment-score"></div><div class="comment-text"><p>Sorry about how I have been submitting my responses. I didn't realize what you had written in the parenthesis was for me.</p><p>Regarding the Duration column in Conversations, do you know if that is in seconds?</p><p>Thanks for your responses.</p></div><div id="comment-6384-info" class="comment-info"><span class="comment-age">(15 Sep '11, 04:11)</span> gakar06</div></div></div><div id="comment-tools-6356" class="comment-tools"></div><div class="clear"></div><div id="comment-6356-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

