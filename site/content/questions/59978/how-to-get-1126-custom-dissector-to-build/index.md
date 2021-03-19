+++
type = "question"
title = "how to get 1.12.6 custom dissector to build"
description = '''Hi all, I have the packet-ospf.c, packet-rsvp.c and few other dissectors customized with 1.12.6 load. I need to update this dissectors to add more properitory cases. I have installed the wireshark development environment and got 2.3.0 code from GIT. However my 1.12.6 customized dissector won&#x27;t build...'''
date = "2017-03-10T05:39:00Z"
lastmod = "2017-03-11T04:20:00Z"
weight = 59978
keywords = [ "1.12.6", "dissector", "build" ]
aliases = [ "/questions/59978" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to get 1.12.6 custom dissector to build](/questions/59978/how-to-get-1126-custom-dissector-to-build)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59978-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59978-score" class="post-score" title="current number of votes">0</div><span id="post-59978-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I have the packet-ospf.c, packet-rsvp.c and few other dissectors customized with 1.12.6 load. I need to update this dissectors to add more properitory cases. I have installed the wireshark development environment and got 2.3.0 code from GIT. However my 1.12.6 customized dissector won't build in this environment since the APIs have changed from 1.12.6 load.</p><p>Instead of modifying the APIs to align with the 2.x.x version of Wireshark, do you know if I could still get the 1.12.6 build environment setup and build 1.12.6 with my additional customized dissector changes? I had used "git clone <a href="https://code.wireshark.org/review/wireshark">https://code.wireshark.org/review/wireshark"</a> to get the source code, however this gives the latest source code, so I was not sure how to get the 1.12.6 environment for build.</p><p>Thanks for your inputs!!</p><p>Regards Sanj</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-1.12.6" rel="tag" title="see questions tagged &#39;1.12.6&#39;">1.12.6</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Mar '17, 05:39</strong></p><img src="https://secure.gravatar.com/avatar/f9240775213c2976f22cafb258a453dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanj123&#39;s gravatar image" /><p><span>Sanj123</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanj123 has no accepted answers">0%</span></p></div></div><div id="comments-container-59978" class="comments-container"></div><div id="comment-tools-59978" class="comment-tools"></div><div class="clear"></div><div id="comment-59978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59980"></span>

<div id="answer-container-59980" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59980-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59980-score" class="post-score" title="current number of votes">1</div><span id="post-59980-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Presuming you used <code>git clone</code> to clone the wireshark repository, then use git to checkout the 1.12.6 tag to get that version:</p><pre><code>git checkout tags/wireshark-1.12.6 -b my-1.12.6</code></pre><p>Note the above command creates a branch for you to work in and commit to. Normally this is done so you can easily rebase your changes onto change from the upstream remote, but as 1.12.x is no longer supported that won't be happening, but it is still "best practice".</p><p>Using the above you can condemn your users to working with an obsolete unsupported version of Wireshark as long as you desire to (or they put up with it). You could try using the 1.12.13 tag as that is the latest tag of the 1.12.x version and your plugins should still compile on that with no extra effort on your part.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Mar '17, 06:23</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-59980" class="comments-container"><span id="59981"></span><div id="comment-59981" class="comment"><div id="post-59981-score" class="comment-score"></div><div class="comment-text"><p>Sometimes it's necessary to use older versions, as it was in <a href="https://ask.wireshark.org/questions/59670/extract-particular-register-from-series-of-modbus-packets">this case</a>. I don't know if that applies here though.</p></div><div id="comment-59981-info" class="comment-info"><span class="comment-age">(10 Mar '17, 06:40)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="59982"></span><div id="comment-59982" class="comment"><div id="post-59982-score" class="comment-score"></div><div class="comment-text"><p>Some times it's better to bite the bullet and diff the changes you made to the dissector to the old original and reapply them to the latest version modifying to use the new api's where needed.</p></div><div id="comment-59982-info" class="comment-info"><span class="comment-age">(10 Mar '17, 06:53)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="59989"></span><div id="comment-59989" class="comment"><div id="post-59989-score" class="comment-score"></div><div class="comment-text"><p>The server where 1.12.6 branch was cloned is no longer available. I just have the modified plugins which now need to be modified with additional decoding.</p><p>Could you please let me know the path to clone the 1.12.6 repository?</p><p>"&gt;cd C:\Development</p><blockquote><p>git clone <a href="https://code.wireshark.org/review/wireshark">https://code.wireshark.org/review/wireshark"</a> clones the latest 2.3.x branch which won't work for me.</p></blockquote><p>Thanks</p><p>Sanj</p></div><div id="comment-59989-info" class="comment-info"><span class="comment-age">(10 Mar '17, 08:12)</span> <span class="comment-user userinfo">Sanj123</span></div></div><span id="60003"></span><div id="comment-60003" class="comment"><div id="post-60003-score" class="comment-score"></div><div class="comment-text"><p>The git clone command retrieves the entire repository with all tagged versions. Did you try the <code>git checkout ...</code> command I gave?</p></div><div id="comment-60003-info" class="comment-info"><span class="comment-age">(11 Mar '17, 04:20)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-59980" class="comment-tools"></div><div class="clear"></div><div id="comment-59980-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

