+++
type = "question"
title = "Save a sorted file using Wireshark"
description = '''I have sorted my 822 MB pcap file by source IP address in ascending order using Wireshark (I tried with tshark on command line, using |sort, but nothing would happen, stalled, had to ^C). Bt now I need to save that sorted display to another pcap file for further filtering. I tried Export&amp;gt;Specifie...'''
date = "2016-11-19T22:33:00Z"
lastmod = "2016-11-20T01:20:00Z"
weight = 57472
keywords = [ "sorted", "save", "display", "fie", "to" ]
aliases = [ "/questions/57472" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Save a sorted file using Wireshark](/questions/57472/save-a-sorted-file-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57472-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57472-score" class="post-score" title="current number of votes">0</div><span id="post-57472-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have sorted my 822 MB pcap file by source IP address in ascending order using Wireshark (I tried with tshark on command line, using |sort, but nothing would happen, stalled, had to ^C). Bt now I need to save that sorted display to another pcap file for further filtering. I tried Export&gt;Specified Packets ,and Export&gt;Packet Dissections, and both save the original file, the unsorted one. How can I save this sorted display? Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sorted" rel="tag" title="see questions tagged &#39;sorted&#39;">sorted</span> <span class="post-tag tag-link-save" rel="tag" title="see questions tagged &#39;save&#39;">save</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span> <span class="post-tag tag-link-fie" rel="tag" title="see questions tagged &#39;fie&#39;">fie</span> <span class="post-tag tag-link-to" rel="tag" title="see questions tagged &#39;to&#39;">to</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '16, 22:33</strong></p><img src="https://secure.gravatar.com/avatar/b3f6579bb81c4e2875f9293da09b05c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MaryR&#39;s gravatar image" /><p><span>MaryR</span><br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MaryR has no accepted answers">0%</span></p></div></div><div id="comments-container-57472" class="comments-container"></div><div id="comment-tools-57472" class="comment-tools"></div><div class="clear"></div><div id="comment-57472-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57477"></span>

<div id="answer-container-57477" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57477-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57477-score" class="post-score" title="current number of votes">0</div><span id="post-57477-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>One (slow) way to obtain that goal would be to use scripting. The suggestion below is not tested so you'll probably have to debug it.</p><p>At first pass, you'd obtain the list of all source addresses occurring in the capture file, something like:</p><pre><code>ip_list = $(tshark -r your/capture/file -T fields -e ip.src | sort -u)</code></pre><p>and prepare an empty pcap file to merge the rest with:</p><pre><code>tshark -r your/capture/file -Y usb -w your/result/file</code></pre><p>Next, you would use a "foreach" cycle over the list:</p><pre><code>for ip in $ip_list ; do
    tshark -r your/capture/file -Y &quot;ip.src == $ip&quot; -w /tmp/aux_in_file
    mergecap -a your/result/file /tmp/aux/in_file -w /tmp/aux_out_file
    mv /tmp/aux_out_file your/result/file
done</code></pre><p>Clarifications:</p><ul><li><p><code>-Y usb</code> is an example of a display filter which won't let a single frame through if the input has been captured on an Ethernet interface</p></li><li><p>without <code>-w file/name</code>, <code>tshark</code> produces a <strong>text</strong> output, one line per frame, and sends it to <code>stdout</code> so you pipe it to <code>sort</code>; with <code>-w file/name</code>, the output is a <strong>pcap(ng)-formatted file</strong> and there is nothing on <code>stdout</code> that <code>sort</code> could handle.</p></li><li><p>the <code>-a</code> option to <code>mergecap</code> makes it <strong>append</strong> the second input file to the first one, rather than actually merging them, i.e. ordering frames from both up to their timestamps, which is the default behaviour.</p></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '16, 01:20</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-57477" class="comments-container"></div><div id="comment-tools-57477" class="comment-tools"></div><div class="clear"></div><div id="comment-57477-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

