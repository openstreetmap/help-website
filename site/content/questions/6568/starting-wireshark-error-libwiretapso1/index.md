+++
type = "question"
title = "starting wireshark error libwiretap.so.1"
description = '''I downloaded Wireshark 1.6.2 from this website. I just compiled in Ubuntu 10.4. No errors during build, but an error on start: less@hiv1:/$ wireshark wireshark: error while loading shared libraries: libwiretap.so.1: cannot open shared object file: No such file or directory  or  less@hiv1:/$ sudo wir...'''
date = "2011-09-26T12:51:00Z"
lastmod = "2017-05-24T04:48:00Z"
weight = 6568
keywords = [ "development" ]
aliases = [ "/questions/6568" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [starting wireshark error libwiretap.so.1](/questions/6568/starting-wireshark-error-libwiretapso1)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6568-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6568-score" class="post-score" title="current number of votes">1</div><span id="post-6568-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I downloaded Wireshark 1.6.2 from this website. I just compiled in Ubuntu 10.4. No errors during build, but an error on start:</p><pre><code>[email protected]:/$ wireshark
wireshark: error while loading shared libraries: libwiretap.so.1: cannot open shared object file: No such file or directory</code></pre><p>or</p><pre><code>[email protected]:/$ sudo wireshark
wireshark: error while loading shared libraries: libwiretap.so.1: cannot open shared object file: No such file or directory</code></pre><p>Anything missing that I should install? Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '11, 12:51</strong></p><img src="https://secure.gravatar.com/avatar/61b159ba087c8d193268cc507adbb21a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cjejuni&#39;s gravatar image" /><p><span>cjejuni</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cjejuni has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Sep '11, 21:46</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6568" class="comments-container"></div><div id="comment-tools-6568" class="comment-tools"></div><div class="clear"></div><div id="comment-6568-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="8229"></span>

<div id="answer-container-8229" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8229-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8229-score" class="post-score" title="current number of votes">10</div><span id="post-8229-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I had same problem, I found the solution.Run the following commands</p><pre><code>sudo ldconfig
wireshark</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jan '12, 05:33</strong></p><img src="https://secure.gravatar.com/avatar/d436e93f6e91605cddbb145521b36cdd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="new%20for%20ever&#39;s gravatar image" /><p><span>new for ever</span><br />
<span class="score" title="151 reputation points">151</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="new for ever has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Jan '12, 05:34</strong> </span></p></div></div><div id="comments-container-8229" class="comments-container"><span id="34534"></span><div id="comment-34534" class="comment"><div id="post-34534-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much :)</p></div><div id="comment-34534-info" class="comment-info"><span class="comment-age">(09 Jul '14, 22:25)</span> <span class="comment-user userinfo">flora</span></div></div></div><div id="comment-tools-8229" class="comment-tools"></div><div class="clear"></div><div id="comment-8229-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6571"></span>

<div id="answer-container-6571" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6571-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6571-score" class="post-score" title="current number of votes">1</div><span id="post-6571-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Did you install Wireshark (as root) via "<code>make install</code>", or are you trying to run it right from the build directory? If you are trying to run it from the build directory, then reading <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSrcRunFirstTime.html">section 3.6.1 of the developer's guide</a> might help you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '11, 18:13</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-6571" class="comments-container"></div><div id="comment-tools-6571" class="comment-tools"></div><div class="clear"></div><div id="comment-6571-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="61590"></span>

<div id="answer-container-61590" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61590-score" class="post-score" title="current number of votes">0</div><span id="post-61590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>ya i tryied with this command , it's working fine thanks for posting</p><pre><code>sudo ldconfig
wireshark</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '17, 04:48</strong></p><img src="https://secure.gravatar.com/avatar/d9dc47c601cc1c419ac53f1c5944f239?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jagannathan&#39;s gravatar image" /><p><span>jagannathan</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jagannathan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 May '17, 05:50</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-61590" class="comments-container"></div><div id="comment-tools-61590" class="comment-tools"></div><div class="clear"></div><div id="comment-61590-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

