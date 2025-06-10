+++
type = "question"
title = "How do I map an island in a lake using iD editor and the multipolygon tag"
description = '''How do I map an island in a lake using iD and the multipolygon tag?  I am asking with reference to this other question (islands-in-lakes-not-showing), I found it would not render an island because it did not have a mutipolygon tag. I fixed it with Potlatch2. The original questioner is new and using ...'''
date = "2013-05-19T08:47:00Z"
lastmod = "2014-06-18T23:31:00Z"
weight = 22542
keywords = [ "ideditor", "island", "relations", "multipolygon" ]
aliases = [ "/questions/22542" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do I map an island in a lake using iD editor and the multipolygon tag](/questions/22542/how-do-i-map-an-island-in-a-lake-using-id-editor-and-the-multipolygon-tag)

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
<span id="post-22542-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22542-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-22542-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do I map an island in a lake using iD and the <span>multipolygon</span> tag?</p>
<p>I am asking with reference to <a href="/questions/22483/islands-in-lakes-not-showing">this other question (islands-in-lakes-not-showing)</a>, I found it would not render an island because it did not have a mutipolygon tag. I fixed it with Potlatch2. The original questioner is new and using iD. I tried iD to find out how but no luck.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-island" rel="tag" title="see questions tagged &#39;island&#39;">island</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 May '13, 08:47</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Aug '14, 21:22</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-22542" class="comments-container">
&#10;</div>
<div id="comment-tools-22542" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22542-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="34123"></span>

<div id="answer-container-34123" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34123-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34123-score" class="post-score" title="current number of votes">
11
</div>
<span id="post-34123-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Although the "iD cannot handle relations so far" answer was 100% correct at the time, it now can (sort-of) handle multipolygon relations.</p>
<p>Here's what I think you need to do:</p>
<ol>
<li>Add the area for the outer (the lake in your case) and tag it as a lake</li>
<li>Add the area for the inner. You don't need to add any tags here.</li>
<li>shift-select both.</li>
<li>The radial menu should have a "+" on that ("merge", keyboard shortcut C). Press that. You should have created a multipolygon.</li>
<li>Of course, save, if you are satisfied.</li>
</ol>
<p>One that I created on the test server using this method is here:</p>
<p><a href="http://api06.dev.openstreetmap.org/relation/4295222887">http://api06.dev.openstreetmap.org/relation/4295222887</a></p>
<p>(it won't render because it's on the test server).</p>
<p>The method above does leave an "area=yes" tag on the inner which, while not wrong, is unnecessary. There may also be a better way to do it - I don't know because unfortunately there's no help in iD worthy of the name and wiki documentation is sadly lacking (I suspect most wiki editors are JOSM users). I did raise <a href="https://github.com/openstreetmap/iD/issues/1971">this</a>, but the iD authors' priorities are elsewhere.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jun '14, 23:31</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Aug '14, 21:19</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-34123" class="comments-container">
&#10;</div>
<div id="comment-tools-34123" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34123-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="22544"></span>

<div id="answer-container-22544" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22544-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22544-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-22544-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As far as I know iD cannot handle relations so far.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 May '13, 09:10</strong></p>
<img src="https://secure.gravatar.com/avatar/a18e2b8eb41515c09bb66159941584bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="malenki&#39;s gravatar image" />
<p><span>malenki</span><br />
<span class="score" title="4713 reputation points"><span>4.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="46 badges"><span class="silver">●</span><span class="badgecount">46</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="malenki has 10 accepted answers">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 May '13, 02:21</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-22544" class="comments-container">
<span id="22548"></span>
<div id="comment-22548" class="comment">
<div id="post-22548-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Seems so, yes. Relation editing is planned for version 1.1 (we now have 1.0.1) (see <a href="https://github.com/systemed/iD/wiki/1.1-Roadmap">roadmap for version 1.1</a> and <a href="https://github.com/systemed/iD/issues?page=1&amp;state=open">iD issue list</a>).</p>
</div>
<div id="comment-22548-info" class="comment-info">
<span class="comment-age">(19 May '13, 20:31)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="22550"></span>
<div id="comment-22550" class="comment">
<div id="post-22550-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for info guys. I will try out iD some more as it seems quite good. I will tic an answer to "relations" when it is implemented.</p>
</div>
<div id="comment-22550-info" class="comment-info">
<span class="comment-age">(19 May '13, 23:39)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="23104"></span>
<div id="comment-23104" class="comment">
<div id="post-23104-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><span></span><span>@andy mackey</span>: the <a href="http://www.mapbox.com/blog/tuning-openstreetmap-editing-id-editor-1-1/">1.1 beta is released</a> for testing. You can try now.</p>
</div>
<div id="comment-23104-info" class="comment-info">
<span class="comment-age">(07 Jun '13, 22:17)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="23105"></span>
<div id="comment-23105" class="comment">
<div id="post-23105-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thabks i'll try it in a day or so</p>
</div>
<div id="comment-23105-info" class="comment-info">
<span class="comment-age">(07 Jun '13, 23:26)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-22544" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22544-form-container" class="comment-form-container">
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

