+++
type = "question"
title = "Merge files + identifying Ip ID&#x27;s"
description = '''Hello, I have client and server side captures, and I have merged them to find the matching Identification ID&#x27;s. I used that as column and tested. There are about 100k of packets where am I have hard time to find the packets matching. I used Statistics &amp;gt; Compare.. but did not get good information....'''
date = "2014-02-21T09:40:00Z"
lastmod = "2014-02-24T10:47:00Z"
weight = 30087
keywords = [ "identification" ]
aliases = [ "/questions/30087" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Merge files + identifying Ip ID's](/questions/30087/merge-files-identifying-ip-ids)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30087-score" class="post-score" title="current number of votes">0</div><span id="post-30087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have client and server side captures, and I have merged them to find the matching Identification ID's. I used that as column and tested. There are about 100k of packets where am I have hard time to find the packets matching. I used Statistics &gt; Compare.. but did not get good information.</p><p>Needed your inputs to achieve this.</p><p>Regards Prabh</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-identification" rel="tag" title="see questions tagged &#39;identification&#39;">identification</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Feb '14, 09:40</strong></p><img src="https://secure.gravatar.com/avatar/c22dc24aa4525350fe8d06dbbc0c6cb7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="prabh&#39;s gravatar image" /><p><span>prabh</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="prabh has no accepted answers">0%</span></p></div></div><div id="comments-container-30087" class="comments-container"><span id="30088"></span><div id="comment-30088" class="comment"><div id="post-30088-score" class="comment-score"></div><div class="comment-text"><p>Why are you trying to find the matching IP IDs? What is it that you are ultimately trying to accomplish?</p></div><div id="comment-30088-info" class="comment-info"><span class="comment-age">(21 Feb '14, 13:07)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div></div><div id="comment-tools-30087" class="comment-tools"></div><div class="clear"></div><div id="comment-30087-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30142"></span>

<div id="answer-container-30142" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30142-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30142-score" class="post-score" title="current number of votes">0</div><span id="post-30142-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can print the IP IDs with tshark and then use a script (perl, python, whatever) or a spreadsheet software to find duplicate values.</p><blockquote><p>tshark -nr input.pcap -T fields -e frame.number -e ip.id -E header=yes -E separator=; &gt; ip_id.txt</p></blockquote><p>Sample output:</p><pre><code>frame.number;ip.id
1;0xf038
2;0x95c0
3;0xf039
4;0x95c0</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Feb '14, 10:47</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Feb '14, 10:48</strong> </span></p></div></div><div id="comments-container-30142" class="comments-container"></div><div id="comment-tools-30142" class="comment-tools"></div><div class="clear"></div><div id="comment-30142-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

