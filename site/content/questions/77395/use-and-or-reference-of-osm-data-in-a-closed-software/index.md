+++
type = "question"
title = "Use and or reference of OSM data in a closed software"
description = '''Dear Community, we are evaluating the use of OSM in our products but struggled in our team with the following questions. We would appreciate any kind of Confirmation, Enlightments or any other help! Question 1: How should the physical separation be done in order not to produce a &quot;derivative work&quot;? T...'''
date = "2020-11-04T11:58:00Z"
lastmod = "2020-11-06T23:23:00Z"
weight = 77395
keywords = [ "usage", "derivative", "compliance", "license" ]
aliases = [ "/questions/77395" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Use and or reference of OSM data in a closed software](/questions/77395/use-and-or-reference-of-osm-data-in-a-closed-software)

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
<span id="post-77395-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77395-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77395-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear Community,</p>
<p>we are evaluating the use of OSM in our products but struggled in our team with the following questions. We would appreciate any kind of Confirmation, Enlightments or any other help!</p>
<h1 id="question-1-how-should-the-physical-separation-be-done-in-order-not-to-produce-a-derivative-work">Question 1: How should the physical separation be done in order not to produce a "derivative work"?</h1>
<p>The license speaks of a database. With Ms SQL Server, it is clear what is meant by a database, but parts of a database (e.g. schemas) can be physically stored in different locations. For example, Microsoft logically creates a database, but it can be physically separated. Is the physical storage decisive in the end? NoSql databases consider schemata as independent databases.</p>
<p>So if I follow these arguments, then the following variations are only "<strong>Collective Databases</strong>"? If OSM data is stored in:</p>
<ul>
<li>a separate (logical) Microsoft SQL database?</li>
<li>a separate schema (e.g. with the name or table) within the application database?</li>
<li>a separate table (e.g. with the meta-name _ODBL__ before the actual table name: (e.g. schema.applicationsdatabase.schema.odbl_Tablename)?</li>
</ul>
<p>And only a table mixed with own and OSM data would be a "<strong>Derivative Work</strong>"?</p>
<p>In search of a solution we found this answer from an <a href="https://help.openstreetmap.org/users/104/frederik-ramm">OSM Moderator</a>:<br />
<a href="/questions/16559/unclear-on-derivative-db-vs-produced-work-vs-collective-db">"<em>One thing that is clear though is that when ODbL talks of databases, it always talks of the concept, and never of the manifestation. This means that whether your two databases reside in different buildings, or on the same computer but different database engines, or in the same engine but different tables, or even in the same table, does not make a difference for the "derivative database" question; whether one is a derivative of the other depends on what you do with it, not how you store it.</em>"</a> <sup>1</sup></p>
<p><br />
</p>
<h1 id="question-2-can-i-use-parts-of-a-result-based-on-calculations-of-osm-data-without-triggering-share-alike-to-the-application-database">Question 2: Can I use parts of a result based on calculations of OSM data without triggering Share-Alike to the application database?</h1>
<p>A specially created database (which we place under ODbL v1.0) which we would call <strong>OSMResults</strong> is composed of the following columns, among others:</p>
<table>
<tbody>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Source</th>
</tr>
&#10;<tr>
<td style="text-align: left;">ID</td>
<td style="text-align: left;">self generated</td>
</tr>
<tr>
<td style="text-align: left;">FromId</td>
<td style="text-align: left;">OSM</td>
</tr>
<tr>
<td style="text-align: left;">ToId</td>
<td style="text-align: left;">OSM</td>
</tr>
<tr>
<td style="text-align: left;">DistanceByAir</td>
<td style="text-align: left;">OSM</td>
</tr>
<tr>
<td style="text-align: left;">DistanceByLand</td>
<td style="text-align: left;">OSM</td>
</tr>
<tr>
<td style="text-align: left;">NeededDriveTime</td>
<td style="text-align: left;">self calculated based on OSM Data</td>
</tr>
</tbody>
</table>
<p><br />
Now an application would calculate an area to be displayed on the basis of the travel times (<em>NeededDriveTime</em>) and the location information of a customer from another data source and displays it on a map by colored highlighting ("<strong>Produced Work</strong>"?). The result is also stored in the application database ("<strong>Derivative Work</strong>"?).<br />
The stored information is:<br />
</p>
<ul>
<li>the calculated OSM result (<em>NeededDriveTime</em>)</li>
<li><em>Id</em> of the area</li>
<li>Coordinates of the colored area and the area information</li>
<li>if necessary, further customer-specific or external data.</li>
</ul>
<p>If <strong>NONE</strong> <em>explicit</em> OSM data (i.e. pure OSM data) is stored in the application database, but only the calculated results (<em>NeededDriveTime</em>, <em>ID</em>) is it a "<strong>Collective Database</strong>" or a "<strong>Derivative Work</strong>"?</p>
<p><br />
</p>
<h1 id="question-3-what-if-we-just-reference-the-osm-data-or-its-calculated-results">Question 3: What if we just "reference" the OSM data or its calculated results?</h1>
<p>If in this case the original data nor the calculated results would not be stored in the application database, but only references to the external database <strong>OSMResults</strong> are used, is the application database a "<strong>collective database</strong>"? Or are the references equivalent to an interaction and lead to the fact that the calculation of the area also becomes a "<strong>Derivative Work</strong>"?</p>
<p><a href="https://wiki.osmfoundation.org/wiki/Licence/Licence_and_Legal_FAQ#What_exactly_do_I_need_to_share.3F">"<em>This data does not have to be shared, provided there <u><strong>is no interaction</strong></u> with the OpenStreetMap derived layer. For example, you cannot have a layer of restaurant icons that only appear if the same restaurant is not in OpenStreetMap!</em>"</a> <sup>2</sup></p>
<p><br />
</p>
<p>To a similar question an <a href="https://help.openstreetmap.org/users/104/frederik-ramm">OSM Moderator</a> answered:<br />
<a href="/questions/17932/collective-produced-derivative-work">"<em>If you manage to create your algorithm in a way that the mixing of OSM and proprietary data happens on-the-fly when the user queries your system, then it is likely that you are not creating a derived database and therefore you don't have to share anything except the original OSM data you've been using.&gt;<br />
<br />
The ODbL doesn't require that you make the exact snapshot of the database available, it is ok to have a reasonable delay.</em><br />
<em>I repeat that this is a non-lawyer opinion from someone who has been wrong in the past.</em>"</a> <sup>3</sup></p>
<p><br />
</p>
<h1 id="sources">Sources:</h1>
<p><sup>1</sup> <a href="/questions/16559/unclear-on-derivative-db-vs-produced-work-vs-collective-db">https://help.openstreetmap.org/questions/16559/unclear-on-derivative-db-vs-produced-work-vs-collective-db</a><br />
<sup>2</sup> <a href="https://wiki.osmfoundation.org/wiki/Licence/Licence_and_Legal_FAQ#What_exactly_do_I_need_to_share.3F">https://wiki.osmfoundation.org/wiki/Licence/Licence_and_Legal_FAQ#What_exactly_do_I_need_to_share.3F</a><br />
<sup>3</sup> <a href="/questions/17932/collective-produced-derivative-work">https://help.openstreetmap.org/questions/17932/collective-produced-derivative-work</a><br />
</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-usage" rel="tag" title="see questions tagged &#39;usage&#39;">usage</span> <span class="post-tag tag-link-derivative" rel="tag" title="see questions tagged &#39;derivative&#39;">derivative</span> <span class="post-tag tag-link-compliance" rel="tag" title="see questions tagged &#39;compliance&#39;">compliance</span> <span class="post-tag tag-link-license" rel="tag" title="see questions tagged &#39;license&#39;">license</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Nov '20, 11:58</strong></p>
<img src="https://secure.gravatar.com/avatar/f7a117b47ab311d9d18539e2b7993186?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="birgos&#39;s gravatar image" />
<p><span>birgos</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="birgos has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-77395" class="comments-container">
<span id="77423"></span>
<div id="comment-77423" class="comment">
<div id="post-77423-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As a footnote, the role you describe as "OSM Moderator" has no special authority over use of the database. The reason you see "Moderator" by their name is that they have given enough helpful answers to questions to earn the privilege of editing questions and answers on <em>this help site</em> alone. Nothing more.</p>
</div>
<div id="comment-77423-info" class="comment-info">
<span class="comment-age">(06 Nov '20, 20:45)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-77395" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77395-form-container" class="comment-form-container">
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

<span id="77413"></span>

<div id="answer-container-77413" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77413-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-77413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you need specific legal advice, then you need to ask a lawyer.</p>
<p>Otherwise, if you want to ask the community here, then you'll receive similar answers to the ones you have already quoted! For example, as I read question 1 I was thinking that "it doesn't really matter what exact technical method you use to store the data, what really matters is whether the two databases are conceptually derived from one or other" but that's just a less clear version of the answer that you have already found.</p>
<p>So I'm not sure what, if anything, we can add to the answers that you've already found!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Nov '20, 15:55</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span> </br></br></p>
</div>
</div>
<div id="comments-container-77413" class="comments-container">
<span id="77424"></span>
<div id="comment-77424" class="comment">
<div id="post-77424-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Note that there is a large body of relevant guidance provided by the OSMF here <a href="https://wiki.osmfoundation.org/wiki/Licence/Community_Guidelines">https://wiki.osmfoundation.org/wiki/Licence/Community_Guidelines</a></p>
</div>
<div id="comment-77424-info" class="comment-info">
<span class="comment-age">(06 Nov '20, 23:23)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-77413" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77413-form-container" class="comment-form-container">
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

