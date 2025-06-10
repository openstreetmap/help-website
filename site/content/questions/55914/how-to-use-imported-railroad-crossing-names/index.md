+++
type = "question"
title = "How to Use Imported &quot;Railroad Crossing Names&quot;"
description = '''From the GNIS Import, there are many names which (I am assuming) are railroad crossing locations. This situation may be limited to US-ian users, from what I understand of GNIS data. In one example that I am seeing, there is one called Martin Crossing which is located by a straight stretch of Martin ...'''
date = "2017-04-27T14:08:00Z"
lastmod = "2017-04-28T15:24:00Z"
weight = 55914
keywords = [ "crossing", "railway", "place", "lifecycle", "tagging" ]
aliases = [ "/questions/55914" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to Use Imported "Railroad Crossing Names"](/questions/55914/how-to-use-imported-railroad-crossing-names)

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
<span id="post-55914-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55914-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-55914-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>From the GNIS Import, there are many names which (I am assuming) are railroad crossing locations. This situation may be limited to US-ian users, from what I understand of GNIS data.</p>
<p>In one example that I am seeing, there is one called Martin Crossing which is located by a straight stretch of Martin Road. Now here is the tricky bit: This railroad area has been unused for many, many years and the path is only used by the occasional hiker. There is not any indication that there was a railroad crossing here except for the name. So, how should this be modified? The import defaulted all GNIS nodes as place=HAMLET which is just obviously wrong.</p>
<ol>
<li>Delete the whole thing. The railroad crossing is gone and the name should go with it.</li>
<li>Change the <strong>place=hamlet</strong> to <strong>place=neighborhood</strong> or <strong>place=locality</strong></li>
<li>Use a motorway junction node (inappropriate) <strong>junction=yes</strong> , <strong>name=Martin Crossing</strong></li>
<li>Use railway tags, with the lifecycle <em>disused</em> prefix: <strong>disused:railway=level_crossing</strong> , <strong>name=Martin Crossing</strong></li>
</ol>
<p>I am also finding references to railroad station names, from the import as well, such as the Fremont Station place=hamlet. I have been changing them to place=neighborhood nodes, but it really "grinds my gears" that these railroad names will be continued to be used by OSM users, simply because some import brought in some data about an infrastructure that no longer exists. I would enjoy deleting them, but I recognize this is information might be interesting from a historical perspective. What are other people doing with there situations?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-crossing" rel="tag" title="see questions tagged &#39;crossing&#39;">crossing</span> <span class="post-tag tag-link-railway" rel="tag" title="see questions tagged &#39;railway&#39;">railway</span> <span class="post-tag tag-link-place" rel="tag" title="see questions tagged &#39;place&#39;">place</span> <span class="post-tag tag-link-lifecycle" rel="tag" title="see questions tagged &#39;lifecycle&#39;">lifecycle</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Apr '17, 14:08</strong></p>
<img src="https://secure.gravatar.com/avatar/cb68523a12e3580728c6bee495ae602e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtc&#39;s gravatar image" />
<p><span>mtc</span><br />
<span class="score" title="411 reputation points">411</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtc has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Apr '17, 15:15</strong> </span></p>
</div>
</div>
<div id="comments-container-55914" class="comments-container">
<span id="55920"></span>
<div id="comment-55920" class="comment">
<div id="post-55920-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>mtc, maybey a bit late, but do you have a picture of it or a link ?</p>
</div>
<div id="comment-55920-info" class="comment-info">
<span class="comment-age">(27 Apr '17, 15:51)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
</div>
<div id="comment-tools-55914" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55914-form-container" class="comment-form-container">
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

<span id="55919"></span>

<div id="answer-container-55919" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55919-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-55919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mtc has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If there's not a trace of it on the ground then I'd certainly not map anything that points to a railway crossing, past or present. Remember that if you delete the node from OSM (which is what I would do) you don't delete the information from the face of the Earth - someone who is interested in doing historical research could, and likely will, still use the GNIS data set and/or OpenHistoricalMap.</p>
<p>If there's an indication that the <em>name</em> is still in use locally ("I saw a flock of pheasants out there by Martin Crossing") then a <code>place=locality</code> might be borderline acceptable (I say "borderline" because there's nothing on the ground that makes this verifiable - but if local people agree the place is called by that name then I guess it's good enough). A tag of <code>place=neighbourhood</code> would not be right.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Apr '17, 14:58</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-55919" class="comments-container">
<span id="55936"></span>
<div id="comment-55936" class="comment">
<div id="post-55936-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your thoughts. I can see how this is the correct approach, now. I do fret about deleting data, though. See my comment below about how OSM / GNIS references are getting into the local language use, so it becomes impossible to say there is no local use, since the locals use the OSM / GNIS name data.</p>
<p>I also appreciate your insights into limiting place=neighborhood and place=locality. I know that I have been using neighbourhoods for non-urban areas, when I was trying to save some of this GNIS import data. I wish there were some better guidelines for handling those nodes. I have contacted the importer "Beej" a couple times, who believes these nodes are a starting point for local mappers, to be changed as appropriate. Unfortunately, what is appropriate in each situation can be rather tricky.</p>
</div>
<div id="comment-55936-info" class="comment-info">
<span class="comment-age">(28 Apr '17, 15:24)</span> <span class="comment-user userinfo">mtc</span>
</div>
</div>
</div>
<div id="comment-tools-55919" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55919-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55918"></span>

<div id="answer-container-55918" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55918-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55918-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55918-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If it definitely a railroad-related feature, then using a railway tag makes sense. railway=level_crossing is for where a road and railway cross. If this is a junction of rails, then railway=switch would be better, or if a place where rails cross but don't connect, railway=railway_crossing.</p>
<p>If railroad tags don't seem appropriate, I wouldn't change these to place=neighborhood, as that is likely inaccurate. According to the wiki, a neighborhood is a named part of an urban area. As you've described these locations, place=locality would be better as it's for "an unpopulated named place".</p>
<p>It's hard to make a call about deleting or not without local knowledge. In a way keeping these visible might allow local mappers to notice the name and delete it or fix it as appropriate.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Apr '17, 14:56</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-55918" class="comments-container">
<span id="55921"></span>
<div id="comment-55921" class="comment">
<div id="post-55921-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The GNIS information was likely sourced from USGS topographic maps, in this case some version of <a href="https://ngmdb.usgs.gov/img4/ht_icons/Browse/NH/NH_Epping_329550_1995_24000.jpg">https://ngmdb.usgs.gov/img4/ht_icons/Browse/NH/NH_Epping_329550_1995_24000.jpg</a> (by the freeway junction on the bottom half of the image).</p>
<p>I haven't looked into it much, but such names do seem to be whatever the railway called the spot more than anything else. Locally many such places have grown into small settlements.</p>
</div>
<div id="comment-55921-info" class="comment-info">
<span class="comment-age">(27 Apr '17, 16:40)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="55922"></span>
<div id="comment-55922" class="comment">
<div id="post-55922-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, the examples along the former railway line there are pretty clearly names used by the railroad. However, that is no guarantee that they are still called by that name so some research or local knowledge is really preferred.</p>
</div>
<div id="comment-55922-info" class="comment-info">
<span class="comment-age">(27 Apr '17, 17:03)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="55935"></span>
<div id="comment-55935" class="comment">
<div id="post-55935-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>In regards to a railroad-related feature, this location was originally a railroad-related feature, but has been abandoned by that company. All that remains is a long, empty swath of land that stretches from town to town. Here is an article on the topic for that town:</p>
<p><a href="http://thisweekinraymond.com/walking-east-to-epping-on-the-rockingham-rail-trail-p4620-169.htm">http://thisweekinraymond.com/walking-east-to-epping-on-the-rockingham-rail-trail-p4620-169.htm</a></p>
<p>In regards to the local use of the name, I am actually a local. It is my opinion that the occasional local use of these names come from people using online maps, such as OSM, which have imported this GNIS data! I see them mentioned on real estate listings and other sources that collect data online, but cannot recollect pre-Internet usage. The amount of usage of these GNIS terms depends on whether there are other commonly used names and notable locations for the area. The GNIS terms are creeping into local language as net-savvy outsiders immigrate to the local community. So that leads to the complicated question, should OSM mappers use the local language of the community that gets their language from OSM? I answer this myself with the mantra, "Map what is visibly verifiable on-the-ground."</p>
</div>
<div id="comment-55935-info" class="comment-info">
<span class="comment-age">(28 Apr '17, 15:09)</span> <span class="comment-user userinfo">mtc</span>
</div>
</div>
</div>
<div id="comment-tools-55918" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55918-form-container" class="comment-form-container">
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

