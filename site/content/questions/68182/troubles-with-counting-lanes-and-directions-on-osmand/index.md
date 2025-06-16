+++
type = "question"
title = "Troubles with counting lanes and directions on OsmAnd"
description = '''Hello everyone!  I&#x27;ve inserted every [turn:lanes] info that I know in one important highway which I use daily, but when I saw it on OsmAnd (I&#x27;ve got OsmAnd Live and have hourly updates) the lanes weren&#x27;t exactely the way I&#x27;ve putted in on OSM.  In a lot of intersections on the app it appears as 6 or...'''
date = "2019-02-27T19:50:00Z"
lastmod = "2019-03-02T08:31:00Z"
weight = 68182
keywords = [ "rendering", "osmand", "turnlanes" ]
aliases = [ "/questions/68182" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Troubles with counting lanes and directions on OsmAnd](/questions/68182/troubles-with-counting-lanes-and-directions-on-osmand)

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
<span id="post-68182-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68182-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68182-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone!</p>
<p>I've inserted every [turn:lanes] info that I know in one important highway which I use daily, but when I saw it on OsmAnd (I've got OsmAnd Live and have hourly updates) the lanes weren't exactely the way I've putted in on OSM.</p>
<p>In a lot of intersections on the app it appears as 6 or even 11 lanes, when it's actually only 3 or 4 (that info is specify on [lanes]) like you can see on the screenshot below <img src="/upfiles/Screenshot_20190223-160359.png" alt="alt text" /></p>
<p>I'd like help to know what's possible wrong there and what needs to be corrected before I start to insert [turn:lanes] info into more roads of my city.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-osmand" rel="tag" title="see questions tagged &#39;osmand&#39;">osmand</span> <span class="post-tag tag-link-turnlanes" rel="tag" title="see questions tagged &#39;turnlanes&#39;">turnlanes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Feb '19, 19:50</strong></p>
<img src="https://secure.gravatar.com/avatar/a9af180a5adf954b2d7095c7e3e81e94?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="viimoraees&#39;s gravatar image" />
<p><span>viimoraees</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="viimoraees has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-68182" class="comments-container">
<span id="68185"></span>
<div id="comment-68185" class="comment">
<div id="post-68185-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>This looks like it might be a reoccurance of an old <a href="https://github.com/osmandapp/Osmand/issues/5003">OsmAnd bug</a>. Does disabling and then re-enabling the live updates for that region fix the issue?</p>
</div>
<div id="comment-68185-info" class="comment-info">
<span class="comment-age">(27 Feb '19, 21:21)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="68190"></span>
<div id="comment-68190" class="comment">
<div id="post-68190-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, does indeed look like this bug. However this bug has been fixed and I didn't saw it again after the fix. Weird.</p>
<p><a href="https://help.openstreetmap.org/users/16336/viimoraees">@viimoraees</a> it looks like you are using JOSM. JOSM has a really nice paint style called "Lane and road attributes". It works really well and use it all the time when adding lanes and turn lanes. You will immediately see your changes, before uploading.</p>
</div>
<div id="comment-68190-info" class="comment-info">
<span class="comment-age">(28 Feb '19, 08:27)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="68208"></span>
<div id="comment-68208" class="comment">
<div id="post-68208-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/4426/insertuser">@InsertUser</a> Is exactly this bug! Disabling and re-enabling the live updates didn't fix it :( first I thought that was something wrong I've done in editing, but luckily it's not my fault.</p>
<p><a href="https://help.openstreetmap.org/users/158/scai">@scai</a> I do use this paint style! It does help a lot when mapping the lanes.</p>
</div>
<div id="comment-68208-info" class="comment-info">
<span class="comment-age">(01 Mar '19, 18:12)</span> <span class="comment-user userinfo">viimoraees</span>
</div>
</div>
<span id="68215"></span>
<div id="comment-68215" class="comment">
<div id="post-68215-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/16336/viimoraees">@viimoraees</a> from the bug thread; the issue may be due to conflicting live updates. Turning off and re-enabling <em>all</em> updates doesn't purge the old files, it just prevents further updates. On my device, opening the country specific listing and turning off the Live update for that region warns that the update files will be deleted. I think this is what you want as it will remove the conflict. When you re-add the region to the list of regions that get updates it should then only download the latest version (and hopefully clear the bug).</p>
</div>
<div id="comment-68215-info" class="comment-info">
<span class="comment-age">(02 Mar '19, 08:31)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-68182" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68182-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

