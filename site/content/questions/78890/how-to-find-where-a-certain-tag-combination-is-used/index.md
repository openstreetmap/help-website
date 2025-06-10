+++
type = "question"
title = "How to find where a certain tag combination is used?"
description = '''I&#x27;m looking for some live examples of the tag use area:highway=motorway. Can see in Taginfo map view generated with Overpass Turbo (?) that the bulk of the 4400 is in a block from somewhere in/near the Netherlands to round about Poland, mostly Northern Germany area so I can find out how they&#x27;ve over...'''
date = "2021-02-17T10:22:00Z"
lastmod = "2021-02-17T23:22:00Z"
weight = 78890
keywords = [ "highway", "area" ]
aliases = [ "/questions/78890" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to find where a certain tag combination is used?](/questions/78890/how-to-find-where-a-certain-tag-combination-is-used)

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
<span id="post-78890-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78890-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78890-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking for some live examples of the tag use area:highway=motorway. Can see in Taginfo map view generated with Overpass Turbo (?) that the bulk of the 4400 is in a block from somewhere in/near the Netherlands to round about Poland, mostly Northern Germany area so I can find out how they've overcome the reported 'no feature tag ways' issue. My skills are just too limited beyond hit and miss finding in OSM</p>
<p>The discussion of the tag is in wiki <a href="https://wiki.openstreetmap.org/wiki/Key:area:highway">https://wiki.openstreetmap.org/wiki/Key:area:highway</a> and I've used it twice for motorway exit areas, one of them <a href="https://wiki.openstreetmap.org/wiki/Key:area:highway">https://wiki.openstreetmap.org/wiki/Key:area:highway</a> <a href="https://www.openstreetmap.org/way/864557206">https://www.openstreetmap.org/way/864557206</a> copycatting the tag from Milano Sud motorway toll gate area. Only tags on the items I created are area:highway=motorway, name and surface. What additional tag is needed on this is the quest. Splitting in area=yes and highway=motorway does not resolve the issue.</p>
<p>TIA for any help on this.</p>
<p>PS: Significantly the meaning which escapes me is the wiki line "The tag requires the linear, routable direction of the highway mapped in addition as lines with highway=*." suggesting a direction tag is needed.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Feb '21, 10:22</strong></p>
<img src="https://secure.gravatar.com/avatar/ed39ace8cbefe3b5c45da98f60f5e34c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SekeRob&#39;s gravatar image" />
<p><span>SekeRob</span><br />
<span class="score" title="211 reputation points">211</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SekeRob has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Feb '21, 10:28</strong> </span></p>
</div>
</div>
<div id="comments-container-78890" class="comments-container">
&#10;</div>
<div id="comment-tools-78890" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78890-form-container" class="comment-form-container">
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

<span id="78893"></span>

<div id="answer-container-78893" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78893-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78893-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-78893-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SekeRob has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>taginfo processes OpenStreetMap data directly to produce those maps. The Overpass Turbo button launches Overpass Turbo with a premade query for finding the tag-value combination: <a href="https://overpass-turbo.eu/s/13LG">https://overpass-turbo.eu/s/13LG</a> (click run to see the results).</p>
<p>On the results map at Overpass Turbo, clicking one of the overlaid objects opens an info panel that includes a link to the OpenStreetMap page for the object.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Feb '21, 11:56</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-78893" class="comments-container">
<span id="78895"></span>
<div id="comment-78895" class="comment">
<div id="post-78895-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Many thanks, that worked. Unfortunately not got any the wiser after perusing a dozen. Some mappers went out into a huge effort of literally drawing the physical outlines of motorways and bridges (Die Autobahn). Bridges I've done for which there is though a different bridge area tag to which all on the bridge can be related, structure, support, type etc. Only difference in one instance was that area=yes was in addition to area:highway=motorway. Makes no sense, but i'll try and see if the duh moment arrives.</p>
<p>thanks again</p>
<p>PS none of them had an Osmose bubble warning on them, crossing fingers.</p>
</div>
<div id="comment-78895-info" class="comment-info">
<span class="comment-age">(17 Feb '21, 13:00)</span> <span class="comment-user userinfo">SekeRob</span>
</div>
</div>
<span id="78905"></span>
<div id="comment-78905" class="comment">
<div id="post-78905-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Just curious, but why do you think there need to be any additional tags? Tagging it with area:highway=motorway is sufficient according to the wiki. Surface makes sense and you've already added that. Name probably shouldn't be on the area, though.</p>
<p>Just a reminder based on your past questions that the QA tools only highlight things that COULD be issues. Some may not be. Not everything on Osmose needs to be (or should be) fixed.</p>
</div>
<div id="comment-78905-info" class="comment-info">
<span class="comment-age">(17 Feb '21, 17:40)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="78906"></span>
<div id="comment-78906" class="comment">
<div id="post-78906-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes I'm aware, they [Osmose] themselves say so that they're not the gospel and false positives are well possible. I just like to cross the T's and dot the I's. What's even more puzzling is some get flagged and some don't... validation bug(?). Anyway, area=yes + highway=motorway gets a warning as well. Now waiting after a fiddle if the green blob comes back again.</p>
</div>
<div id="comment-78906-info" class="comment-info">
<span class="comment-age">(17 Feb '21, 18:36)</span> <span class="comment-user userinfo">SekeRob</span>
</div>
</div>
<span id="78915"></span>
<div id="comment-78915" class="comment">
<div id="post-78915-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Yes, area=yes + highway=motorway would definitely not be correct, since that would be like a plaza or square where you can move in any direction... at motorway speeds.</p>
</div>
<div id="comment-78915-info" class="comment-info">
<span class="comment-age">(17 Feb '21, 23:22)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-78893" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78893-form-container" class="comment-form-container">
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

