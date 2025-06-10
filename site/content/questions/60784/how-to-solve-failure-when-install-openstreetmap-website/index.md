+++
type = "question"
title = "How to solve failure when install openstreetmap website?"
description = '''Hello, I follow the guide on github to install my openstreetmap website. But when I run bundle exec rake test:db, a failure occurred: Failure: AmfControllerTest#test_getway_old [/home/yeager/sfw/openstreetmap-website/test/controllers/amf_controller_test.rb:350]: Expected: 0 Actual: -1  Is there anyo...'''
date = "2017-11-26T00:43:00Z"
lastmod = "2017-12-06T19:17:00Z"
weight = 60784
keywords = [ "openstreetmap", "website", "install", "failure" ]
aliases = [ "/questions/60784" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to solve failure when install openstreetmap website?](/questions/60784/how-to-solve-failure-when-install-openstreetmap-website)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60784-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60784-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60784-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I follow the guide on github to install my openstreetmap website. But when I run bundle exec rake test:db, a failure occurred:</p>
<pre><code>Failure:
AmfControllerTest#test_getway_old [/home/yeager/sfw/openstreetmap-website/test/controllers/amf_controller_test.rb:350]:
Expected: 0
Actual: -1</code></pre>
<p>Is there anyone met the same question? How to solve it? Thanks for your help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-website" rel="tag" title="see questions tagged &#39;website&#39;">website</span> <span class="post-tag tag-link-install" rel="tag" title="see questions tagged &#39;install&#39;">install</span> <span class="post-tag tag-link-failure" rel="tag" title="see questions tagged &#39;failure&#39;">failure</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Nov '17, 00:43</strong></p>
<img src="https://secure.gravatar.com/avatar/66e4305afae2faf808a2b600525c4cc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gleide&#39;s gravatar image" />
<p><span>gleide</span><br />
<span class="score" title="79 reputation points">79</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gleide has one accepted answer">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Dec '17, 20:41</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-60784" class="comments-container">
<span id="60858"></span>
<div id="comment-60858" class="comment">
<div id="post-60858-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>We'll need some more information to help. Is this the only test that fails? Have you installed the three database functions (maptile_for_point etc) mentioned in the INSTALL.md file?</p>
</div>
<div id="comment-60858-info" class="comment-info">
<span class="comment-age">(29 Nov '17, 11:52)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
</div>
<div id="comment-tools-60784" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60784-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61047"></span>

<div id="answer-container-61047" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61047-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61047-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-61047-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This turns out to have been a bug in the way that timezones are handled in the test suite, and has now been fixed. For more information see <a href="https://github.com/openstreetmap/openstreetmap-website/issues/1688">https://github.com/openstreetmap/openstreetmap-website/issues/1688</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Dec '17, 19:17</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-61047" class="comments-container">
&#10;</div>
<div id="comment-tools-61047" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61047-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

