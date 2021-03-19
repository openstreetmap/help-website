+++
type = "question"
title = "Piping tshark output to wireshark"
description = '''I&#x27;m trying to set up a remote capture from a debian box to wireshark running on windows.  I&#x27;m using the following command: plink server -pw pass &quot;tshark -i eth0 -w -&quot; | wireshark.exe -k -i -  Which throws an error on wireshark startup as a popup window saying  No Packets captured!  As no data was ca...'''
date = "2014-08-01T02:04:00Z"
lastmod = "2014-08-01T07:36:00Z"
weight = 35047
keywords = [ "pipe", "remote-capture" ]
aliases = [ "/questions/35047" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Piping tshark output to wireshark](/questions/35047/piping-tshark-output-to-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35047-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35047-score" class="post-score" title="current number of votes">0</div><span id="post-35047-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to set up a remote capture from a debian box to wireshark running on windows. I'm using the following command:</p><pre><code>plink server -pw pass &quot;tshark -i eth0 -w -&quot; | wireshark.exe -k -i -</code></pre><p>Which throws an error on wireshark startup as a popup window saying No Packets captured! As no data was captured, closing the temporary capture file</p><p>And another popup saying:</p><pre><code>Error reading from pipe: Der Vorgang wurde erfolgreich beendet. error 0</code></pre><p>The second sentence translates roughly as: Operation completed succesfully.</p><p>To test that this is not an issue with my ssh connection, i tried piping from tshark to wireshark locally using</p><pre><code>tshark.exe -w - | Wireshark.exe -k -i -</code></pre><p>which leads to the same errors. Any suggestions?</p><p>Edit: Just updated to Wireshark 1.12.0 everything still the same</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pipe" rel="tag" title="see questions tagged &#39;pipe&#39;">pipe</span> <span class="post-tag tag-link-remote-capture" rel="tag" title="see questions tagged &#39;remote-capture&#39;">remote-capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Aug '14, 02:04</strong></p><img src="https://secure.gravatar.com/avatar/691b0d201aa48a003e86465aec40154c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pguetschow&#39;s gravatar image" /><p><span>pguetschow</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pguetschow has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Aug '14, 02:05</strong> </span></p></div></div><div id="comments-container-35047" class="comments-container"></div><div id="comment-tools-35047" class="comment-tools"></div><div class="clear"></div><div id="comment-35047-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35048"></span>

<div id="answer-container-35048" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35048-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35048-score" class="post-score" title="current number of votes">1</div><span id="post-35048-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pguetschow has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark can't read pcap-ng (default output format of tshark) from STDIN.</p><p>please try this:</p><blockquote><p>tshark.exe -F pcap -w - | Wireshark.exe -k -i -</p></blockquote><p>or</p><blockquote><p>plink server -pw pass "tshark -i eth0 -F pcap -w -" | wireshark.exe -k -i -</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '14, 02:14</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-35048" class="comments-container"><span id="35054"></span><div id="comment-35054" class="comment"><div id="post-35054-score" class="comment-score"></div><div class="comment-text"><p>Thanks, this works for the local variant.</p><p>When piping from plink I get an error about "pcap" not being a supported format. choosing libpcap leads to the same behavior as before. Is libpcap a different format and my version of tshark just doesn't know about pcap?</p></div><div id="comment-35054-info" class="comment-info"><span class="comment-age">(01 Aug '14, 04:23)</span> <span class="comment-user userinfo">pguetschow</span></div></div><span id="35057"></span><div id="comment-35057" class="comment"><div id="post-35057-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Is libpcap a different format and my version of tshark just doesn't know about pcap?</p></blockquote><p>it's the same. Your tshark version on Debian is just different than on Windows (there was a rename of the option).</p></div><div id="comment-35057-info" class="comment-info"><span class="comment-age">(01 Aug '14, 05:15)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="35059"></span><div id="comment-35059" class="comment"><div id="post-35059-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the help so far. Do you have any ideas what could cause the the problem when tunneling via ssh? Or is that outside of the scope of AskWireshark?</p></div><div id="comment-35059-info" class="comment-info"><span class="comment-age">(01 Aug '14, 05:25)</span> <span class="comment-user userinfo">pguetschow</span></div></div><span id="35060"></span><div id="comment-35060" class="comment"><div id="post-35060-score" class="comment-score"></div><div class="comment-text"><p>What is the version of the remote copy of tshark?</p></div><div id="comment-35060-info" class="comment-info"><span class="comment-age">(01 Aug '14, 05:30)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="35061"></span><div id="comment-35061" class="comment"><div id="post-35061-score" class="comment-score"></div><div class="comment-text"><p>Tshark 1.8.2</p></div><div id="comment-35061-info" class="comment-info"><span class="comment-age">(01 Aug '14, 05:35)</span> <span class="comment-user userinfo">pguetschow</span></div></div><span id="35066"></span><div id="comment-35066" class="comment not_top_scorer"><div id="post-35066-score" class="comment-score"></div><div class="comment-text"><p>Please try it with tcpdump</p><blockquote><p>plink server -pw pass "tcpdump -ni eth0 -w -"</p></blockquote></div><div id="comment-35066-info" class="comment-info"><span class="comment-age">(01 Aug '14, 07:36)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-35048" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-35048-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

