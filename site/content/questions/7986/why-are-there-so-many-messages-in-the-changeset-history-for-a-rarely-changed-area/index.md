+++
type = "question"
title = "Why are there so many messages in the changeset history for a rarely changed area?"
description = '''On the main site, with mapnik map. If I zoom in to a country side town that has been rarely changed. And then click on the &quot;History&quot; tab to see the Changeset history, I see lots of changesets-messages. Why is that? Example: Changeset for an country side area with almost no map symbols, but still a l...'''
date = "2011-09-18T21:04:00Z"
lastmod = "2012-08-17T10:49:00Z"
weight = 7986
keywords = [ "changeset", "history", "changelog" ]
aliases = [ "/questions/7986" ]
osqa_answers = 5
osqa_accepted = true
+++

<div class="headNormal">

# [Why are there so many messages in the changeset history for a rarely changed area?](/questions/7986/why-are-there-so-many-messages-in-the-changeset-history-for-a-rarely-changed-area)

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
<span id="post-7986-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7986-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-7986-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>On the main site, with mapnik map. If I zoom in to a country side town that has been rarely changed. And then click on the "History" tab to see the Changeset history, I see lots of changesets-messages. Why is that?</p>
<p>Example: <a href="http://www.openstreetmap.org/browse/changesets?bbox=16.4006%2C60.452%2C16.502%2C60.4834">Changeset for an country side area</a> with almost no map symbols, but still a lot of change-set messages.</p>
<p>This makes it hard to use the changeset-history. I think that some of my mapping years ago is removed, so I would like to see the changeset-history.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span> <span class="post-tag tag-link-changelog" rel="tag" title="see questions tagged &#39;changelog&#39;">changelog</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Sep '11, 21:04</strong></p>
<img src="https://secure.gravatar.com/avatar/b1d217a3a6e04cf4654372068beef20d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonas_&#39;s gravatar image" />
<p><span>Jonas_</span><br />
<span class="score" title="662 reputation points">662</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonas_ has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Sep '11, 23:30</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-7986" class="comments-container">
&#10;</div>
<div id="comment-tools-7986" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7986-form-container" class="comment-form-container">
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

5 Answers:

</div>

</div>

<span id="7987"></span>

<div id="answer-container-7987" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7987-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7987-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-7987-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jonas_ has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The history tab shows all changesets where the bounding box of the changeset intersects the bounding box of your map display. This usually includes many changesets that affected data on a world-wide scale, e.g. making just one edit on each continent will create very big bounding box!</p>
<p>It is good style to avoid such large changesets but still they do happen. There is a much better tool than the history view, called <a href="http://wiki.openstreetmap.org/wiki/OWL_%28OpenStreetMap_Watch_List%29">OWL,</a> that does not have this problem; OWL should only highlight changesets that really have affected the area in question.</p>
<p>OWL is still under development but once it is stable, the plan is to replace the current history view with one generated by OWL.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Sep '11, 21:17</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-7987" class="comments-container">
&#10;</div>
<div id="comment-tools-7987" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7987-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7993"></span>

<div id="answer-container-7993" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7993-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7993-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-7993-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>ITO's <a href="http://www.itoworld.com/static/openstreetmap_tools/osm_mapper.html">OSM Mapper</a> application also allows you to "watch" an area in a similar way to OWL. Like OWL, it only shows actual changes with the area that you're interested in, not those that have a huge bounding box that incorporates it.</p>
<p>It doesn't yet track deletes though, so it won't find who deleted some stuff of yours unless the person that did it also added something new.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Sep '11, 23:36</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-7993" class="comments-container">
&#10;</div>
<div id="comment-tools-7993" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7993-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15184"></span>

<div id="answer-container-15184" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15184-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15184-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-15184-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Note at the moment the OWL service seems some what defunct.</p>
<p>There is a new 'service' that goes some way to remove massive bounding box changes that cover the area in question, working from the basic OSM history feed.</p>
<p><a href="http://positron96.appspot.com/osmfilter.html">http://positron96.appspot.com/osmfilter.html</a></p>
<p>Hopefully one day OWL will come back and be part of the core OSM services.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '12, 00:12</strong></p>
<img src="https://secure.gravatar.com/avatar/074785ea4eae108f0e4e89456bf74737?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robbieonsea&#39;s gravatar image" />
<p><span>robbieonsea</span><br />
<span class="score" title="904 reputation points">904</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robbieonsea has 4 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-15184" class="comments-container">
&#10;</div>
<div id="comment-tools-15184" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15184-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8017"></span>

<div id="answer-container-8017" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8017-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8017-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8017-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you mapped in the area, you can then identify the changesets that you created and then find the nodes, ways etc that you created. You can then look at thier history and see if they have been changed, moved or deleted by someone else since you created them.<br />
Use the link to 'Your user page' and the 'my edits' link to do this. Paging through your edits may find your changeset if you know when the changes were made or have a helpfull comment. If you don't know when the change was made but can identify the area, adding a bounding box to the search may help. So for the link you provided try the <a href="http://www.openstreetmap.org/user/Jonas_/edits?box=yes&amp;maxlat=60.4834&amp;maxlon=16.502&amp;minlat=60.452&amp;minlon=16.4006">following</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Sep '11, 14:17</strong></p>
<img src="https://secure.gravatar.com/avatar/6edb4957e57770118c3b8022cfce68a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srbrook&#39;s gravatar image" />
<p><span>srbrook</span><br />
<span class="score" title="993 reputation points">993</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srbrook has 3 accepted answers">13%</span> </br></p>
</div>
</div>
<div id="comments-container-8017" class="comments-container">
&#10;</div>
<div id="comment-tools-8017" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8017-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15206"></span>

<div id="answer-container-15206" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15206-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15206-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15206-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the Potlach2 editor it's easy to find who as worked on a way.</p>
<ol>
<li>Enter edit mode</li>
<li>Highlight way</li>
<li>Click on advanced tab (bottom of tagging box)</li>
<li>Click on way number (top on tagging box)</li>
<li>You should now see edit history of that way</li>
<li>Highlight one from list</li>
<li>Click see more details</li>
</ol>
<p>Hope this helps</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '12, 10:49</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Aug '12, 22:59</strong> </span></p>
</div>
</div>
<div id="comments-container-15206" class="comments-container">
&#10;</div>
<div id="comment-tools-15206" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15206-form-container" class="comment-form-container">
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

