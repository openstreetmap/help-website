+++
type = "question"
title = "Splitting pcap files in wireshark"
description = '''After review a 2GB pcap file in wireshark, is there anyway can split file in half. I tried r running editcap from root; but got message &quot;Less data was read than was expected&quot; using the latest version of Wireshark.'''
date = "2014-09-24T22:43:00Z"
lastmod = "2014-09-25T19:24:00Z"
weight = 36580
keywords = [ "files", "pcap", "splitting", "ask.wireshark.org", "in" ]
aliases = [ "/questions/36580" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Splitting pcap files in wireshark](/questions/36580/splitting-pcap-files-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36580-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36580-score" class="post-score" title="current number of votes">0</div><span id="post-36580-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>After review a 2GB pcap file in wireshark, is there anyway can split file in half. I tried r running editcap from root; but got message "Less data was read than was expected" using the latest version of Wireshark.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-files" rel="tag" title="see questions tagged &#39;files&#39;">files</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-splitting" rel="tag" title="see questions tagged &#39;splitting&#39;">splitting</span> <span class="post-tag tag-link-ask.wireshark.org" rel="tag" title="see questions tagged &#39;ask.wireshark.org&#39;">ask.wireshark.org</span> <span class="post-tag tag-link-in" rel="tag" title="see questions tagged &#39;in&#39;">in</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '14, 22:43</strong></p><img src="https://secure.gravatar.com/avatar/e4e65789b62967213583302c83e93a63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Z2869&#39;s gravatar image" /><p><span>Z2869</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Z2869 has no accepted answers">0%</span></p></div></div><div id="comments-container-36580" class="comments-container"></div><div id="comment-tools-36580" class="comment-tools"></div><div class="clear"></div><div id="comment-36580-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="36586"></span>

<div id="answer-container-36586" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36586-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36586-score" class="post-score" title="current number of votes">0</div><span id="post-36586-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"editcap -c 100000 in.pcap out.pcap" usually works fine for me - what kind of parameters did you use?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '14, 01:02</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-36586" class="comments-container"><span id="36603"></span><div id="comment-36603" class="comment"><div id="post-36603-score" class="comment-score"></div><div class="comment-text"><p>Jasper, I tried what you suggested but only got one record, not sure what I doing wrong. Do you have a good contact number if you wouldn't mind sharing. vr Jamie</p></div><div id="comment-36603-info" class="comment-info"><span class="comment-age">(25 Sep '14, 09:58)</span> <span class="comment-user userinfo">Z2869</span></div></div></div><div id="comment-tools-36586" class="comment-tools"></div><div class="clear"></div><div id="comment-36586-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="36596"></span>

<div id="answer-container-36596" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36596-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36596-score" class="post-score" title="current number of votes">0</div><span id="post-36596-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As Jasper said, editcap should work.</p><p>But you could also do it from the GUI. For example if you have a 100-packet capture you want to split in half:</p><ol><li>Use a display filter of "frame.number &lt; 50"</li><li>File-&gt;Export Specified Packets</li><li>Only export the displayed packets</li><li>Repeat 1-3 with a filter of "frame.number &gt;= 50"</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '14, 06:12</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-36596" class="comments-container"><span id="36600"></span><div id="comment-36600" class="comment"><div id="post-36600-score" class="comment-score"></div><div class="comment-text"><p>Jasper and Jeff, Kudos. I did just that same and got the message ""Less data was read than was expected", I tried reloaded same capture and got same "error message" Jeff I will give your idea as try. I am so thank for both of your replies. I will let you folks know how it goes. vr Jamie</p></div><div id="comment-36600-info" class="comment-info"><span class="comment-age">(25 Sep '14, 07:52)</span> <span class="comment-user userinfo">Z2869</span></div></div><span id="36614"></span><div id="comment-36614" class="comment"><div id="post-36614-score" class="comment-score"></div><div class="comment-text"><p>I got it to work but had to do alot of playing with &gt; and = values etc. I wsa able to find or write a script to split files, have well over 4TB to do. :-(</p></div><div id="comment-36614-info" class="comment-info"><span class="comment-age">(25 Sep '14, 12:14)</span> <span class="comment-user userinfo">Z2869</span></div></div><span id="36616"></span><div id="comment-36616" class="comment"><div id="post-36616-score" class="comment-score"></div><div class="comment-text"><p>Hmm if you have that much data you really should be using editcap. I'd suggest opening a <a href="https://bugs.wireshark.org">bug report</a> about editcap (including a sample capture, of course) and/or trying out the <a href="https://www.wireshark.org/download/automated/">latest buildbot version</a> of Wireshark to see if the problem is already fixed.</p><p>That being said, it's also possible that it could be done with tshark but I couldn't tell you if you need the "-R" or "-Y" argument (there's some funniness with tshark and frame numbers depending on how you're doing your filtering--and I don't remember the conclusion of those discussions).</p></div><div id="comment-36616-info" class="comment-info"><span class="comment-age">(25 Sep '14, 12:41)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-36596" class="comment-tools"></div><div class="clear"></div><div id="comment-36596-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="36620"></span>

<div id="answer-container-36620" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36620-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36620-score" class="post-score" title="current number of votes">0</div><span id="post-36620-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Kudos Jeff will follow up after to do as you suggest as well check latest build v. Thanks for taking time to follow up with me. v/r Jamie</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '14, 19:24</strong></p><img src="https://secure.gravatar.com/avatar/e4e65789b62967213583302c83e93a63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Z2869&#39;s gravatar image" /><p><span>Z2869</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Z2869 has no accepted answers">0%</span></p></div></div><div id="comments-container-36620" class="comments-container"></div><div id="comment-tools-36620" class="comment-tools"></div><div class="clear"></div><div id="comment-36620-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

