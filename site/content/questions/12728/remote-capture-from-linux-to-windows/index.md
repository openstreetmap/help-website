+++
type = "question"
title = "Remote Capture from Linux to Windows"
description = '''Am trying to set up remote capture from Linux (on a Amazon EC2 VM) to my Windows 7 laptop. I have found a couple of commands that claim to work using the plink SSH client that comes with Putty. Number 1: plink PersonEC2 &#x27; sudo tshark -i eth0 &amp;gt; /tmp/pipe &#x27; | wireshark -k –i  where PersonEC2 is my ...'''
date = "2012-07-15T13:06:00Z"
lastmod = "2012-07-16T07:58:00Z"
weight = 12728
keywords = [ "capture", "remote" ]
aliases = [ "/questions/12728" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Remote Capture from Linux to Windows](/questions/12728/remote-capture-from-linux-to-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12728-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12728-score" class="post-score" title="current number of votes">0</div><span id="post-12728-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Am trying to set up remote capture from Linux (on a Amazon EC2 VM) to my Windows 7 laptop. I have found a couple of commands that claim to work using the plink SSH client that comes with Putty.</p><p>Number 1: plink PersonEC2 ' sudo tshark -i eth0 &gt; /tmp/pipe ' | wireshark -k –i where PersonEC2 is my Putty Saved Session Name</p><p>Number 2: wireshark -k -i &lt; (plink –ssh <a href="http://XXXX.compute-1.amazonaws.com">XXXX.compute-1.amazonaws.com</a> -l ubuntu sudo /usr/bin/tshark -i eth0 -w ) where XXXX is the public IP address for my VM</p><p>Neither command works. (The keys are working fine, so that is no problem getting logged in.)</p><p>I have successfully executed "plink PersonEC2 sudo tshark -i eth0 -w /out.cap" from a cmd window on my laptop. This successfully starts tshark and captures packets in out.cap. I have successfully copied out.cap from the Linux VM to my Win7 laptop and opened the file in Wireshark. But when I try to add the pipe in Number 1 to feed Wireshark on my laptop directly, I get a message from the cmd box on my laptop saying "The system cannot find the path specified." Number 2 gives the same error message.</p><p>Am I on the right track with either of these two and can someone help me further. It seems like I still have two steps to go: 1) getting the tshark command on the Linux VM to accept a pipe as output and then getting my Win7 copy of Wireshark hooked up to the pipe.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-remote" rel="tag" title="see questions tagged &#39;remote&#39;">remote</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '12, 13:06</strong></p><img src="https://secure.gravatar.com/avatar/2e191fa849fae16953fd75342a9a11bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KenHadley&#39;s gravatar image" /><p><span>KenHadley</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KenHadley has no accepted answers">0%</span></p></div></div><div id="comments-container-12728" class="comments-container"></div><div id="comment-tools-12728" class="comment-tools"></div><div class="clear"></div><div id="comment-12728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12734"></span>

<div id="answer-container-12734" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12734-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12734-score" class="post-score" title="current number of votes">2</div><span id="post-12734-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>On Linux you need to write the output to STDOUT to be able to read it on Windows.</p><p>Please try this:</p><blockquote><p><code>plink PersonEC2 'sudo tshark -i eth0 -w - ' | wireshark -k –i -</code><br />
</p></blockquote><p><strong>UPDATE</strong>: If sudo prompts for a password, this could cause problems (as sudo will also write to STDOUT). In that case, login (ssh/plink) with the root account directly!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '12, 00:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Jul '12, 05:56</strong> </span></p></div></div><div id="comments-container-12734" class="comments-container"><span id="12766"></span><div id="comment-12766" class="comment"><div id="post-12766-score" class="comment-score"></div><div class="comment-text"><p>Thank you. That is just what I needed.</p></div><div id="comment-12766-info" class="comment-info"><span class="comment-age">(16 Jul '12, 07:58)</span> <span class="comment-user userinfo">KenHadley</span></div></div></div><div id="comment-tools-12734" class="comment-tools"></div><div class="clear"></div><div id="comment-12734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

