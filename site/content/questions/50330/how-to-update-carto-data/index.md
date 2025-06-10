+++
type = "question"
title = "[closed] How to update carto data"
description = '''HI We used carto data for generate tiles. But it shows AndhraPradesh &amp;amp; Telungana as a single state.(Actually these are two different states in India). How to update my carto data? Also how to get latest carto data?'''
date = "2016-06-20T11:00:00Z"
lastmod = "2016-06-23T16:24:00Z"
weight = 50330
keywords = [ "boundaries", "admin_boundary", "tiles", "carto", "tileserver" ]
aliases = [ "/questions/50330" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] How to update carto data](/questions/50330/how-to-update-carto-data)

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
<span id="post-50330-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50330-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50330-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>HI</p>
<p>We used carto data for generate tiles.</p>
<p>But it shows AndhraPradesh &amp; Telungana as a single state.(Actually these are two different states in India).</p>
<p>How to update my carto data? Also how to get latest carto data?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-carto" rel="tag" title="see questions tagged &#39;carto&#39;">carto</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jun '16, 11:00</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>01 Nov '16, 10:29</strong> </span></p>
</div>
</div>
<div id="comments-container-50330" class="comments-container">
<span id="50337"></span>
<div id="comment-50337" class="comment">
<div id="post-50337-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Can you explain what you mean by "We used carto data"? There are both companies and map styles (and probably much more) called that.</p>
</div>
<div id="comment-50337-info" class="comment-info">
<span class="comment-age">(20 Jun '16, 15:17)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="50395"></span>
<div id="comment-50395" class="comment">
<div id="post-50395-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/387/someoneelse"></a><a href="http://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> Oh! Sorry I wrongly understood as carto is a separate data which was used for show borders/regions. Now i understand as carto is a tool which will parse osm data then generate a boundary data and stored in DB, while tiles generation we can use this boundary data for show regions(only in land not in sea). right?</p>
<p>Also now i tried with latest OSM data for india, but there is no seperate region/border for Telungana &amp; AndhraPradesh. How can we update state regions in OSM?</p>
</div>
<div id="comment-50395-info" class="comment-info">
<span class="comment-age">(23 Jun '16, 07:35)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
<span id="50397"></span>
<div id="comment-50397" class="comment">
<div id="post-50397-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>We've had Telangana <a href="http://www.openstreetmap.org/relation/3250963/history">in our databases since before it was officially a separate state</a></p>
<p>So either you're using a seperate databases for borders which is out of date, or your update failed.</p>
</div>
<div id="comment-50397-info" class="comment-info">
<span class="comment-age">(23 Jun '16, 08:40)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
<span id="50415"></span>
<div id="comment-50415" class="comment">
<div id="post-50415-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/10142/joost-schouppe">@joost schouppe</a> : Thanks for your reply. Yes my data not updated properly. How to update this carto data? I am doing as 1.delete carto_boundary table, 2.generate carto_boundary.sql, 3.exec psql -f carto_boundary.sql -d &lt;db_name&gt;. Is it correct ?</p>
</div>
<div id="comment-50415-info" class="comment-info">
<span class="comment-age">(23 Jun '16, 16:24)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
</div>
<div id="comment-tools-50330" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50330-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "The question is answered, right answer was accepted" by Rajavelu_M 01 Nov '16, 10:29

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50411"></span>

<div id="answer-container-50411" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50411-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50411-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-50411-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>"carto is a tool which will parse osm data then generate a boundary data and stored in DB, while tiles generation we can use this boundary data" is mostly correct. Actually it's a bit more complicated than that, due to the history of what happened with OSM's "standard" style.</p>
<p>The second part " while tiles generation we can use this boundary data for show regions(only in land not in sea)" has actually been answer elsewhere (someone else asked a similar quesion):</p>
<p><a href="http://help.openstreetmap.org/questions/50367/can-i-exclude-the-district-borders-extending-on-ocean-in-admin_level-5/50386">http://help.openstreetmap.org/questions/50367/can-i-exclude-the-district-borders-extending-on-ocean-in-admin_level-5/50386</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jun '16, 13:07</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jun '16, 13:08</strong> </span></p>
</div>
</div>
<div id="comments-container-50411" class="comments-container">
&#10;</div>
<div id="comment-tools-50411" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50411-form-container" class="comment-form-container">
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

