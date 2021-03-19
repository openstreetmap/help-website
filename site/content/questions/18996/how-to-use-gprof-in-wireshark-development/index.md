+++
type = "question"
title = "How to use gprof in wireshark development."
description = '''I&#x27;m development on the wireshark1.8.5. I have to find the function which cost a lot of time when wireshark is running. Thanks!'''
date = "2013-02-28T18:34:00Z"
lastmod = "2013-06-14T11:16:00Z"
weight = 18996
keywords = [ "profile", "gprof" ]
aliases = [ "/questions/18996" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to use gprof in wireshark development.](/questions/18996/how-to-use-gprof-in-wireshark-development)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18996-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18996-score" class="post-score" title="current number of votes">0</div><span id="post-18996-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm development on the wireshark1.8.5.</p><p>I have to find the function which cost a lot of time when wireshark is running.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-profile" rel="tag" title="see questions tagged &#39;profile&#39;">profile</span> <span class="post-tag tag-link-gprof" rel="tag" title="see questions tagged &#39;gprof&#39;">gprof</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '13, 18:34</strong></p><img src="https://secure.gravatar.com/avatar/f6eeed42d5aadabfed2ca2cb1faabff1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smilezuzu&#39;s gravatar image" /><p><span>smilezuzu</span><br />
<span class="score" title="20 reputation points">20</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smilezuzu has no accepted answers">0%</span></p></div></div><div id="comments-container-18996" class="comments-container"><span id="18997"></span><div id="comment-18997" class="comment"><div id="post-18997-score" class="comment-score"></div><div class="comment-text"><p>or how to use performance profile on vs2010 to find out ?</p></div><div id="comment-18997-info" class="comment-info"><span class="comment-age">(28 Feb '13, 18:36)</span> <span class="comment-user userinfo">smilezuzu</span></div></div><span id="19000"></span><div id="comment-19000" class="comment"><div id="post-19000-score" class="comment-score"></div><div class="comment-text"><p>If you are using Linux, you could do 'valgrind --tool=callgrind --trace-children=yes ./wireshark' then afterwards browse the biggest of the resulting callgrind files using kcachegrind.</p></div><div id="comment-19000-info" class="comment-info"><span class="comment-age">(28 Feb '13, 18:59)</span> <span class="comment-user userinfo">MartinM</span></div></div></div><div id="comment-tools-18996" class="comment-tools"></div><div class="clear"></div><div id="comment-18996-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22070"></span>

<div id="answer-container-22070" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22070-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22070-score" class="post-score" title="current number of votes">0</div><span id="post-22070-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>On Linux:</p><p>Unpack the source code and run configure with the option <code>--enable-profile-build</code>.</p><blockquote><p><code>./configure --enable-profile-build</code><br />
</p></blockquote><p>Then run Wireshark and do whatever you want to test.</p><p>Exit Wireshark and run the following command from the source directory.</p><blockquote><p>libtool --mode=execute gprof wireshark gmon.out</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '13, 11:16</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-22070" class="comments-container"></div><div id="comment-tools-22070" class="comment-tools"></div><div class="clear"></div><div id="comment-22070-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

