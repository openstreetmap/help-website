+++
type = "question"
title = "Wireshark setup Linux for nonroot user in Amazon Ec2"
description = '''My goal is to capture packets with tshark in Amazon Linux AMI. While typing tshark in the command line there&#x27;s an error: &quot;tshark: There are no interfaces on which a capture can be done&quot;  How to implement the solution : &amp;gt; $ sudo apt-get install wireshark $ &amp;gt; sudo dpkg-reconfigure wireshark-comm...'''
date = "2013-10-29T08:52:00Z"
lastmod = "2013-10-31T04:49:00Z"
weight = 26515
keywords = [ "wireshark", "tshark", "linux" ]
aliases = [ "/questions/26515" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark setup Linux for nonroot user in Amazon Ec2](/questions/26515/wireshark-setup-linux-for-nonroot-user-in-amazon-ec2)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26515-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26515-score" class="post-score" title="current number of votes">0</div><span id="post-26515-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My goal is to capture packets with tshark in Amazon Linux AMI. While typing tshark in the command line there's an error: "tshark: There are no interfaces on which a capture can be done"</p><p>How to implement the solution :</p><pre><code>&gt; $ sudo apt-get install wireshark $
&gt; sudo dpkg-reconfigure wireshark-common
&gt; $ sudo usermod -a -G wireshark $USER $
&gt; gnome-session-quit --logout --no-prompt</code></pre><p>in Amazon Linux AMI (it's not Ubuntu)? Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Oct '13, 08:52</strong></p><img src="https://secure.gravatar.com/avatar/bd81fb6370a901321913b1465efa8e51?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="warrior7089&#39;s gravatar image" /><p><span>warrior7089</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="warrior7089 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Oct '13, 08:53</strong> </span></p></div></div><div id="comments-container-26515" class="comments-container"></div><div id="comment-tools-26515" class="comment-tools"></div><div class="clear"></div><div id="comment-26515-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26579"></span>

<div id="answer-container-26579" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26579-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26579-score" class="post-score" title="current number of votes">1</div><span id="post-26579-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How to implement the solution in Amazon Linux AMI (it's not Ubuntu)?</p></blockquote><p>Amazon AMI is based on CentOS.</p><p>So, please do this:</p><blockquote><p>yum install wireshark<br />
yum install wireshark-gnome<br />
</p></blockquote><p>or maybe for AMI</p><blockquote><p>yum install wireshark-1.2.15</p></blockquote><p>then set the capabilities for dumpcap</p><blockquote><p>sudo setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' /usr/bin/dumpcap</p></blockquote><p>Then run the following command as <strong>non root</strong> user!</p><blockquote><p>dumpcap -D -M</p></blockquote><p>If you see interfaces: problem solved!<br />
</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Oct '13, 04:24</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Oct '13, 04:25</strong> </span></p></div></div><div id="comments-container-26579" class="comments-container"><span id="26582"></span><div id="comment-26582" class="comment"><div id="post-26582-score" class="comment-score"></div><div class="comment-text"><p>Thanks. It works.</p></div><div id="comment-26582-info" class="comment-info"><span class="comment-age">(31 Oct '13, 04:47)</span> <span class="comment-user userinfo">warrior7089</span></div></div><span id="26583"></span><div id="comment-26583" class="comment"><div id="post-26583-score" class="comment-score"></div><div class="comment-text"><p>good.</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-26583-info" class="comment-info"><span class="comment-age">(31 Oct '13, 04:49)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-26579" class="comment-tools"></div><div class="clear"></div><div id="comment-26579-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

