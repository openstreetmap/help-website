+++
type = "question"
title = "Including packets from a conversation not matching the filter"
description = '''I am trying to determine the amount of data received and transmitted back to a remote telematic device that communicates over GPRS on port TCP X to find out if my wireless carrier is overcharging me. The trick is that the server receives data on that same port from several units. Capture filter: tcp...'''
date = "2012-10-19T15:56:00Z"
lastmod = "2012-10-24T17:24:00Z"
weight = 15114
keywords = [ "filter", "packets", "stream", "missing" ]
aliases = [ "/questions/15114" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Including packets from a conversation not matching the filter](/questions/15114/including-packets-from-a-conversation-not-matching-the-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15114-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15114-score" class="post-score" title="current number of votes">0</div><span id="post-15114-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to determine the amount of data received and transmitted back to a remote telematic device that communicates over GPRS on port TCP X to find out if my wireless carrier is overcharging me. The trick is that the server receives data on that same port from several units.</p><p>Capture filter: tcp port X Display filter: tcp contains "6033," and (tcp contains ",1710," or tcp contains ",121017,")</p><p>6033 is the unique identifier for the device I want to get information from, and 1710 or 121017 is the date I'm interested in the two different possible formats included in the TCP stream.</p><p>I'm missing some TCP packets that don't have the string '6033' in them, however they are part of the same TCP stream/conversation and should be included in my filtered results.</p><p>How can I include in my results the missing packets that are part of the TCP stream/conversation BUT don't contain the unique identifier in it?</p><p>i.e. $G6033,1710,232239,5319.4470,N,00627.4218,W,000 1710,232324,5319.4372,N,00627.4342,W,000 1710,232739,5319.4328,N,00627.4310,W,000 1710,232824,5319.4328,N,00627.4310,W,000 1710,233239,5319.4312,N,00627.4129,W,000 1710,233324,5319.4312,N,00627.4129,W,000 1710,233739,5319.4394,N,00627.4296,W,000</p><p>--------- Packet divider (missing from this point on)---------<br />
1710,233824,5319.4243,N,00627.4141,W,000 1710,234239,5319.4326,N,00627.4288,W,000 1710,234324,5319.4326,N,00627.4288,W,000*94<br />
---------- Packet divider (missing until this point)----------</p><p>$A6033,232239,121017,234408*D9</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '12, 15:56</strong></p><img src="https://secure.gravatar.com/avatar/88f148c12acee9290da8b95a85e7468a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="juanclau&#39;s gravatar image" /><p><span>juanclau</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="juanclau has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-15114" class="comments-container"></div><div id="comment-tools-15114" class="comment-tools"></div><div class="clear"></div><div id="comment-15114-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15115"></span>

<div id="answer-container-15115" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15115-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15115-score" class="post-score" title="current number of votes">1</div><span id="post-15115-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As far as I understand this, each unit connects to your server with it's own tcp communication. The "trick" of using always the same port on the server is not really a trick, it is what every server does today (for example the web server of this Q&amp;A page runs on port 80 and takes lots of connections on it). Did you try filtering on the client IP and port instead (meaning the TCP port that the remote device uses)? It is standard filtering operation to isolate TCP flows by filtering on it's socket pairs, or on the unique flow number assigned to each flow by Wireshark.</p><p>So what you'd need to do is:</p><ol><li>filter on the packets that contain the string you're looking for</li><li>use the conversation statistics (found in the statistics menu) to see which communications are left. Use the "limit to display filter" checkbox to force it to only show filtered out packets, and go to the TCP tab.</li><li>filter on each conversation that you see by filtering on it's socket pairs. You can do that from the conversations list by using the popup menu going "apply as filter -&gt; selected -&gt; A &lt;-&gt; B".</li><li>repeat</li></ol><p>You can automate this by using command line scripts with tshark.exe instead, but that might be a bit too complicated for starters.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '12, 07:49</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-15115" class="comments-container"><span id="15233"></span><div id="comment-15233" class="comment"><div id="post-15233-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the quick reply and the help provided.</p><p>When I said "the trick" I referred to the fact that I needed to separate the traffic from different sources, not that traffic was on the same port.</p><p>Unfortunately these are mobile devices that can change their IPs quite often (several times per day), simply using IP filtering is not really the right way to go.</p><p>When I do your suggested solution I get 4 conversations with 4 different IPs. Can I assume the device changed IPs 4 times and the total sum of the 'bytes' column is the amount of data transfer between the server and the mobile device?</p></div><div id="comment-15233-info" class="comment-info"><span class="comment-age">(24 Oct '12, 16:56)</span> <span class="comment-user userinfo">juanclau</span></div></div></div><div id="comment-tools-15115" class="comment-tools"></div><div class="clear"></div><div id="comment-15115-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15122"></span>

<div id="answer-container-15122" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15122-score" class="post-score" title="current number of votes">0</div><span id="post-15122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I'm missing some TCP packets that don't have the string '6033' in them, however they are part of the same TCP stream/conversation and should be included in my filtered results.</p></blockquote><p>O.K. so, you can't use a capture filter. Instead I suggest to record the whole communication and later filter it with a display filter. To automate the process on <strong>Windows</strong>, you can use Powershell.</p><p>Start powershell and enter these commands (without the 'PS &gt;'). input.cap is the capture file containing the whole communication.</p><blockquote><p><code>PS &gt; $display_filter =""; tshark -r input.pcap -R "tcp contains 6033 or tcp contains 1710 or tcp contains 121017" -T fields -e tcp.stream | sort-object | get-unique | foreach { $display_filter += "tcp.stream eq $_ or "}; $display_filter = $display_filter -replace "...$" ; write-host "starting Wireshark with filter: $display_filter" ; wireshark -r input.pcap -R $display_filter</code><br />
</p></blockquote><p>Output should look similar to this:</p><blockquote><p><code>starting Wireshark with filter: tcp.stream eq 13 or tcp.stream eq 14 or tcp.stream eq 9</code><br />
</p></blockquote><p>Wireshark will start with the given display filter and you will see only those streams that contain the search strings.</p><p>If you want to do the same on <strong>Unix</strong>:</p><blockquote><p><code>[email protected]:# tshark -r input.pcap -R "tcp contains 6033 or tcp contains 1710 or tcp contains 121017" -T fields -e tcp.stream | sort -u | awk  '{filter = sprintf("tcp.stream eq %s or %s",$0,filter)}; END {filter=substr(filter,0,length(filter)-3); print filter; system("wireshark -r input.pcap -R \"" filter "\"")}'</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '12, 04:25</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Oct '12, 04:27</strong> </span></p></div></div><div id="comments-container-15122" class="comments-container"><span id="15234"></span><div id="comment-15234" class="comment"><div id="post-15234-score" class="comment-score"></div><div class="comment-text"><p>Kurt,</p><p>Thanks for your answer. Can you explain to me what the command does in a little more detail?</p><p>Also, correct me if I'm wrong but I believe the filter in the command should be: "tcp contains 6033 and (tcp contains 1710 or tcp contains 121017)"</p><p>I can't simply use "tcp contains 6033 or tcp contains 1710 or tcp contains 121017" since that would capture other devices with the same date stamps but a different SID (6033).</p></div><div id="comment-15234-info" class="comment-info"><span class="comment-age">(24 Oct '12, 17:24)</span> <span class="comment-user userinfo">juanclau</span></div></div></div><div id="comment-tools-15122" class="comment-tools"></div><div class="clear"></div><div id="comment-15122-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

