+++
type = "question"
title = "Validation of display filter"
description = '''Our current code provides a GUI which will allow users to create filters. These filters are to be used when performing a live capture or an offline capture when reading a pcap file. We also provide the user with a button which will start Wireshark, reading in a file, performing a display filter and ...'''
date = "2013-06-24T04:49:00Z"
lastmod = "2013-06-24T18:18:00Z"
weight = 22274
keywords = [ "validate", "filters" ]
aliases = [ "/questions/22274" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Validation of display filter](/questions/22274/validation-of-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22274-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22274-score" class="post-score" title="current number of votes">0</div><span id="post-22274-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Our current code provides a GUI which will allow users to create filters. These filters are to be used when performing a live capture or an offline capture when reading a pcap file. We also provide the user with a button which will start Wireshark, reading in a file, performing a display filter and going to a specified packet; I.e. <strong>"C:\Program Files\Wireshark\Wireshark.exe" -R "tcp or udp" -g10 -r "C:\tmp\test.pcap"</strong></p><p>By default, we try to use the same filter when starting Wireshark that was used on this file when we performed an offline capture. We realize that, in some cases, the syntax is different between the "display filter" and the "capture filter". Is there any way we can validate the "display filter" before starting Wireshark? If the validation fails, we'd like to display a popup which would tell the operator, that the filter is invalid and allow them to enter a different filter.</p><p>I.e. <strong>"port 5001"</strong> is a valid capture filter but an illegal display filter. We would like to tell the user that this filter is illegal and give them an opportunity to enter a valid filter.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-validate" rel="tag" title="see questions tagged &#39;validate&#39;">validate</span> <span class="post-tag tag-link-filters" rel="tag" title="see questions tagged &#39;filters&#39;">filters</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jun '13, 04:49</strong></p><img src="https://secure.gravatar.com/avatar/a86b749b12369c6cd191f6eadea1dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sabordn&#39;s gravatar image" /><p><span>sabordn</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sabordn has no accepted answers">0%</span></p></div></div><div id="comments-container-22274" class="comments-container"></div><div id="comment-tools-22274" class="comment-tools"></div><div class="clear"></div><div id="comment-22274-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22275"></span>

<div id="answer-container-22275" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22275-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22275-score" class="post-score" title="current number of votes">0</div><span id="post-22275-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sabordn has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could run tshark in quiet mode to test the filter and then parse the output of tshark and the value of %errorlevel% (Windows)</p><p>Sample of a good filter:</p><blockquote><p>tshark -nr input.pcap -q -R "tcp"<br />
echo %errorlevel%<br />
0</p></blockquote><p>Sample of a wrong filter:</p><blockquote><p>tshark -nr input.pcap -q -R "test"<br />
tshark: "test" is neither a field nor a protocol name.<br />
echo %errorlevel%<br />
2<br />
</p></blockquote><p><strong>UPDATE:</strong></p><p>If you add the option '-c 1' and a 'custom' display filter (frame.number), you are able to test the validity of the user defined display filter pretty fast with tshark.</p><blockquote><p><code>tshark -nr input.pcap -R "frame.number" -R "filter to test" -c 1 -q</code></p></blockquote><p>If the user specified a wrong filter, the whole command will fail (see above).</p><p>If the user specified filter is correct, your own 'custom' filter will abort the command after the first matching packet, which is always the first read packet with the filter 'frame.number'.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '13, 05:07</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Jun '13, 19:05</strong> </span></p></div></div><div id="comments-container-22275" class="comments-container"><span id="22277"></span><div id="comment-22277" class="comment"><div id="post-22277-score" class="comment-score"></div><div class="comment-text"><p>Kurt,</p><p>Thanks for the suggestion. I was hoping there was an easier way to validate the filter (i.e. using the jnetpcap api).</p><p>Your suggestion works. Unfortunately, I'm processing some pcap files that have over a million packets. If the filter is "bad", the process returns immediately, but if the filter is good, it could take minutes to return. I got around this by doing the following:</p><pre><code>Process proc = Runtime.getRuntime().exec(&quot;tshark -nr input.pcap -q -R &quot;tcp&quot;&quot;);
int exitVal = 0;
try {
   exitVal = proc.exitValue();
} catch (IllegalThreadStateException e) {
   proc.destroy();
}</code></pre><p>At this point, I'll just act on the value of exitVal. If exitVal is 0, either it completed successfully or it was running and I destroyed the process. If exitVal is something other than 0, the filter was bad and I'll dispaly a message to the user.</p><p>Do you know of any jnetpcap api that will validate without having to go through this process.</p><p>Thanks, Scott</p></div><div id="comment-22277-info" class="comment-info"><span class="comment-age">(24 Jun '13, 07:22)</span> <span class="comment-user userinfo">sabordn</span></div></div><span id="22278"></span><div id="comment-22278" class="comment"><div id="post-22278-score" class="comment-score"></div><div class="comment-text"><p>(I converted your "answer" to a "comment" as that's how this site works best, please see the FAQ for details.)</p><p>Why not use a synthetic capture file (without any packets, just the pcap file header) to check the filter with tshark?</p></div><div id="comment-22278-info" class="comment-info"><span class="comment-age">(24 Jun '13, 07:38)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="22279"></span><div id="comment-22279" class="comment"><div id="post-22279-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Do you know of any jnetpcap api that will validate without having to go through this process.</p></blockquote><p>As <strong>Wireshark display filters</strong> are a feature of Wireshark, there is no other library to check the validity of a display filter than Wiresharks code itself.</p><p>Please try to add the following option to tshark to speed up this check (see man page):</p><blockquote><p>-c 2</p></blockquote><p>Regards<br />
Kurt</p></div><div id="comment-22279-info" class="comment-info"><span class="comment-age">(24 Jun '13, 07:40)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22280"></span><div id="comment-22280" class="comment not_top_scorer"><div id="post-22280-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@Kurt</span>, that was my initial idea too, however, if the filter does not match any packets in the file, tshark will still read the whole file.</p><p>(-c X means to stop after X displayed packets, not after reading X packets, this was a "bug" I fixed years ago :-) )</p></div><div id="comment-22280-info" class="comment-info"><span class="comment-age">(24 Jun '13, 07:43)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="22286"></span><div id="comment-22286" class="comment"><div id="post-22286-score" class="comment-score">1</div><div class="comment-text"><p>How about modifying Kurt's test slightly:</p><p>A valid filter:</p><pre><code>echo &quot;&quot; | wireshark-gtk2\tshark.exe -2R &quot;tcp&quot; -i -

Capturing on &#39;Standard input&#39;

echo %errorlevel%
0</code></pre><p>An invalid filter:</p><pre><code>echo &quot;&quot; | wireshark-gtk2\tshark.exe -2R &quot;test&quot; -i -

tshark: &quot;test&quot; is neither a field nor a protocol name.

echo %errorlevel%
2</code></pre><p>This should avoid any long delays with reading large capture files.</p></div><div id="comment-22286-info" class="comment-info"><span class="comment-age">(24 Jun '13, 08:32)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="22291"></span><div id="comment-22291" class="comment not_top_scorer"><div id="post-22291-score" class="comment-score"></div><div class="comment-text"><blockquote><p>however, if the filter does not match any packets in the file, tshark will still read the whole file.</p></blockquote><p>ah, good to know. I did not check. I just relied on the text of the man page ;-)</p></div><div id="comment-22291-info" class="comment-info"><span class="comment-age">(24 Jun '13, 09:21)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22297"></span><div id="comment-22297" class="comment not_top_scorer"><div id="post-22297-score" class="comment-score"></div><div class="comment-text"><p>I'd like to thank everyone for their help... Adding the packet count solved my problem. The process returns immediately even with a very large file.</p></div><div id="comment-22297-info" class="comment-info"><span class="comment-age">(24 Jun '13, 11:24)</span> <span class="comment-user userinfo">sabordn</span></div></div><span id="22299"></span><div id="comment-22299" class="comment"><div id="post-22299-score" class="comment-score">1</div><div class="comment-text"><p>Good to hear.</p><p>As of the comment of <span></span><span>@SYN-bit</span>:</p><blockquote><p>if the filter does not match any packets in the file, tshark will still read the whole file.</p></blockquote><p>You can circumvent this problem, by adding a second filter that always matches within the first few packets, like this:</p><blockquote><p><code>tshark -nr input.pcap -R "frame.number" -R "filter to test" -c 1 -q</code></p></blockquote><p>If the user specified filter is wrong, the whole command will fail.</p><p>If the user specified filter is correct, your own filter will abort the command after the first matching packet, which is always the first read packet with the filter 'frame.number'</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-22299-info" class="comment-info"><span class="comment-age">(24 Jun '13, 18:18)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-22275" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-22275-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

