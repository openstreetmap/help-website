+++
type = "question"
title = "Unclear on Derivative DB vs. Produced Work vs. Collective DB"
description = '''I&#x27;m unclear on what I have to redistribute, and when, when combining data from OSM and other sources. I have some data that I need to keep private/non-open, and don&#x27;t want to accidentally convert it to the Open DB License. For example, if I have a list of lat/lon locations, then use OSM data to reve...'''
date = "2012-10-01T05:33:00Z"
lastmod = "2012-10-03T10:45:00Z"
weight = 16559
keywords = [ "data", "legal", "license", "database" ]
aliases = [ "/questions/16559" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unclear on Derivative DB vs. Produced Work vs. Collective DB](/questions/16559/unclear-on-derivative-db-vs-produced-work-vs-collective-db)

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
<span id="post-16559-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16559-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-16559-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm unclear on what I have to redistribute, and when, when combining data from OSM and other sources. I have some data that I need to keep private/non-open, and don't want to accidentally convert it to the Open DB License.</p>
<p>For example, if I have a list of lat/lon locations, then use OSM data to reverse geocode them and store that reverse geocode data, is that a derivative work? What about if I keep the data in separate tables, or separate databases entirely, but use some sort of identifier, (like a foreign key in a relational DB), to say "this is the ID of the lat/lon for the data I reverse geocoded"? It would seem that the two situations likely are derivative works, but I'm not 100% sure.</p>
<p>How separate do data sets have to be to be a collective DB, not a Derivative DB? For example, if I have some data, (say, my reverse geocoded lat/lon list, which I'm assuming is a derivative DB), and I have some private data, if I store both in the same MySQL/Oracle/whatever DB, does my private data become Open DB Licensed?</p>
<p>A large part of my private data is POIs. If I geocode them using OSM data, would they become Open DB Licensed?</p>
<p>I know I've been wordy - thanks for the help. I read through the Legal FAQ page &amp; want to be even more clear on what I can &amp; can't do with OSM data.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-legal" rel="tag" title="see questions tagged &#39;legal&#39;">legal</span> <span class="post-tag tag-link-license" rel="tag" title="see questions tagged &#39;license&#39;">license</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Oct '12, 05:33</strong></p>
<img src="https://secure.gravatar.com/avatar/273e297193c7b955a8bf9feb67f1e1c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jbeales&#39;s gravatar image" />
<p><span>jbeales</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jbeales has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16559" class="comments-container">
&#10;</div>
<div id="comment-tools-16559" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16559-form-container" class="comment-form-container">
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

<span id="16561"></span>

<div id="answer-container-16561" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16561-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-16561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The ODbL is new for us all and we don't have a lot of practical experience with it yet. In some areas it will probably take a while until a common reading is established.</p>
<p>One thing that is clear though is that when ODbL talks of databases, it always talks of the concept, and never of the manifestation. This means that whether your two databases reside in different buildings, or on the same computer but different database engines, or in the same engine but different tables, or even in the same table, does not make a difference for the "derivative database" question; whether one is a derivative of the other depends on what you do with it, not how you store it.</p>
<p>Two databases A and B are clearly collective if nothing in database A has been affected by anything in database B and vice versa. For example, if you have two databases with POIs, one from OSM and one private, and you draw them both onto a map tile, then you're clearly utilising a collective database to make your tile.</p>
<p>I think that the current interpretation of the ODbL is that pure object IDs can never constitute a substantial extract so if you have your private list of POIs and in there you have a column "osm_node_id" that points to an OSM object, that would still be considered ok and you would not be required to release your private database.</p>
<p>Geocoding, specifically, is complex issue and there isn't a clear answer yet. Initial legal advice suggested it would make your database a derivative database (see <a href="http://wiki.openstreetmap.org/wiki/Open_Data_License/Use_Cases">wiki</a>). This is also the position the Legal Working Group has been leaning towards in the meetings where the matter was discussed (meeting minutes <a href="http://www.osmfoundation.org/wiki/Working_Group_Minutes">01 May</a>, <a href="https://docs.google.com/document/pub?id=1Okhbvx3UIzwTlkJ_IUkRStnvyaNvliM4MSsdsRPnjH8">08 May</a>, <a href="https://docs.google.com/document/pub?id=1LW4p1_XvyJWhUtZZk0L_n_io1a0TBZVseodixT2hgT0">15 May</a>, see also <a href="https://docs.google.com/document/pub?id=1Ag81OlT1TtnhYwVE-bBtL018SNoU_V-anG4wLdwMT4c">concept paper</a>). I expect further discussion on that in the near future.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Oct '12, 08:03</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-16561" class="comments-container">
<span id="16584"></span>
<div id="comment-16584" class="comment">
<div id="post-16584-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks. I had figured the ODbL refers to databases conceptually, but I wanted to be clear. I hope that you're right about an "osm_node_id" column in my private database not making it a derivative database, because if it <em>does</em> make it a derivative database, it'll be a pain, (and computationally expensive), to de-dupe my data when actually rendering it, (assuming I use a couple of different map layers to stay compliant).</p>
</div>
<div id="comment-16584-info" class="comment-info">
<span class="comment-age">(01 Oct '12, 17:18)</span> <span class="comment-user userinfo">jbeales</span>
</div>
</div>
<span id="16585"></span>
<div id="comment-16585" class="comment">
<div id="post-16585-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'll look through the links you provided on geocoding. On one hand geocoding is simply an alternative representation of data I already have, since both address data &amp; geocode data indicate a location on the earth, so it shouldn't be a derivative work. On the other hand it takes more than an address to figure out what the geocode is, so it should be a derivative work.</p>
</div>
<div id="comment-16585-info" class="comment-info">
<span class="comment-age">(01 Oct '12, 17:20)</span> <span class="comment-user userinfo">jbeales</span>
</div>
</div>
<span id="16629"></span>
<div id="comment-16629" class="comment">
<div id="post-16629-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I too plan to create a collective database and the definition of what is collective and what is derivative is crucial. If the use of osm_id is fine (and I don't see why it wouldn't be as it's difficult to create a relational database without a key) then I will be happy!</p>
</div>
<div id="comment-16629-info" class="comment-info">
<span class="comment-age">(03 Oct '12, 10:45)</span> <span class="comment-user userinfo">RichardOwen2000</span>
</div>
</div>
</div>
<div id="comment-tools-16561" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16561-form-container" class="comment-form-container">
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

