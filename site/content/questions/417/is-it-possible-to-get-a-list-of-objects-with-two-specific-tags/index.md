+++
type = "question"
title = "Is it possible to get a list of objects with two specific tags?"
description = '''For example, I might want a list of rail trails: objects tagged highway=cycleway and railway=abandoned. The only way I know of doing this is to download all objects with one of those tags and then filter them down, but either unfiltered list will be huge.'''
date = "2010-07-22T02:06:00Z"
lastmod = "2015-01-12T12:52:00Z"
weight = 417
keywords = [ "download", "data" ]
aliases = [ "/questions/417" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to get a list of objects with two specific tags?](/questions/417/is-it-possible-to-get-a-list-of-objects-with-two-specific-tags)

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
<span id="post-417-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-417-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-417-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For example, I might want a list of rail trails: objects tagged highway=cycleway and railway=abandoned. The only way I know of doing this is to download all objects with one of those tags and then filter them down, but either unfiltered list will be huge.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jul '10, 02:06</strong></p>
<img src="https://secure.gravatar.com/avatar/0c334b9f230e39c1e73a2b0322a23fb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NE2&#39;s gravatar image" />
<p><span>NE2</span><br />
<span class="score" title="1359 reputation points"><span>1.4k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NE2 has one accepted answer">9%</span></p>
</div>
</div>
<div id="comments-container-417" class="comments-container">
&#10;</div>
<div id="comment-tools-417" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-417-form-container" class="comment-form-container">
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

<span id="14649"></span>

<div id="answer-container-14649" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14649-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-14649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Meanwhile there is the new <a href="http://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> allowing to search for objects with two or more specific tags, like:</p>
<p><a href="http://www.overpass-api.de/api/xapi?way%5Bhighway=cycleway%5D%5Brailway=abandoned%5D%5B@meta%5D">http://www.overpass-api.de/api/xapi?way[highway=cycleway][railway=abandoned][@meta]</a></p>
<p>(this example uses the <a href="http://wiki.openstreetmap.org/wiki/Overpass_API#XAPI_Compatibility_Layer">XAPI compatibility layer</a>)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jul '12, 13:19</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-14649" class="comments-container">
<span id="40239"></span>
<div id="comment-40239" class="comment">
<div id="post-40239-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>In the meantime it is even simpler: Go to <a href="http://overpass-turbo.eu/">http://overpass-turbo.eu/</a> , position the map, open the wizard, and enter "highway=cycleway AND railway=abandoned". It will automatically generate the needed query code (you may want to remove the "node" line from the code) and show the results on a map. Getting a "list" is a tiny bit more complicated (a real "list" format is not available in its export formats): setting the output <span>to csv</span> would be <a href="/questions/40233/download-establishment-information/40243">possible</a>.</p>
</div>
<div id="comment-40239-info" class="comment-info">
<span class="comment-age">(12 Jan '15, 12:52)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-14649" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14649-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="419"></span>

<div id="answer-container-419" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-419-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-419-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-419-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, it is currently not possible. XAPI as well as the API only support searching for one tag.</p>
<p>Advanced data filtering and manipulation tasks are beyond the scope of our existing APIs. Power users wishing to perform such actions are advised to download the full area of interest, import it into a relational database (for example using Osmosis), and then perform queries on that database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jul '10, 09:23</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jul '10, 14:06</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span></p>
</div>
</div>
<div id="comments-container-419" class="comments-container">
<span id="888"></span>
<div id="comment-888" class="comment">
<div id="post-888-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How do I search even for one tag? For example: name="Metuje". Thanks for help.</p>
</div>
<div id="comment-888-info" class="comment-info">
<span class="comment-age">(21 Sep '10, 16:47)</span> <span class="comment-user userinfo">Kozuch</span>
</div>
</div>
<span id="920"></span>
<div id="comment-920" class="comment">
<div id="post-920-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>@Kozuch: <a href="http://www.informationfreeway.org/api/0.6/*%5Bname=Metuje%5D">http://www.informationfreeway.org/api/0.6/*[name=Metuje]</a> (see <a href="http://wiki.openstreetmap.org/wiki/Xapi">http://wiki.openstreetmap.org/wiki/Xapi</a>)</p>
</div>
<div id="comment-920-info" class="comment-info">
<span class="comment-age">(24 Sep '10, 23:47)</span> <span class="comment-user userinfo">Mormegil</span>
</div>
</div>
</div>
<div id="comment-tools-419" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-419-form-container" class="comment-form-container">
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

