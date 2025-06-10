+++
type = "question"
title = "Change route from Stranraer to Dumfries"
description = '''Hello, The following route Stranraer to Dumfries takes the A712 https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&amp;amp;route=54.9044%2C-5.0262%3B55.0698%2C-3.6092#map=11/54.9930/-4.1521&amp;amp;layers=N Is it possible to have this route take the A75 instead as per google maps? @54.9686155,...'''
date = "2021-02-04T13:02:00Z"
lastmod = "2021-02-05T17:24:00Z"
weight = 78663
keywords = [ "osmchange" ]
aliases = [ "/questions/78663" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Change route from Stranraer to Dumfries](/questions/78663/change-route-from-stranraer-to-dumfries)

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
<span id="post-78663-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78663-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78663-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>The following route Stranraer to Dumfries takes the A712 <a href="https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&amp;route=54.9044%2C-5.0262%3B55.0698%2C-3.6092#map=11/54.9930/-4.1521&amp;layers=N">https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&amp;route=54.9044%2C-5.0262%3B55.0698%2C-3.6092#map=11/54.9930/-4.1521&amp;layers=N</a></p>
<p>Is it possible to have this route take the A75 instead as per google maps? <a href="https://www.google.com/maps/dir/Stranraer/Dumfries/%3Ca%20href=" data-54-north"="" data-6393="" data-help.openstreetmap.org="" https:="" data-users=""></a><a href="https://help.openstreetmap.org/users/6393/54-north">@54</a></a>.9686155,-4.5964665,10z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x486222c5d4b17253:0x20c9568fda8dd62c!2m2!1d-5.024055!2d54.903367!1m5!1m1!1s0x4862b098a2e191d3:0xf6ed72c932b2e2a9!2m2!1d-3.60512!2d55.070859!3e0"&gt;https://www.google.com/maps/dir/Stranraer/Dumfries/<a href="https://help.openstreetmap.org/users/6393/54-north"></a><a href="https://help.openstreetmap.org/users/6393/54-north">@54</a></a>.9686155,-4.5964665,10z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x486222c5d4b17253:0x20c9568fda8dd62c!2m2!1d-5.024055!2d54.903367!1m5!1m1!1s0x4862b098a2e191d3:0xf6ed72c932b2e2a9!2m2!1d-3.60512!2d55.070859!3e0</p>
<p>An obstacle had been reported previously on the A75 by a user with the name Ya Stratospheric. I do not see this note anymore.</p>
<p>Is it possible for this route to take the A75 instead?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmchange" rel="tag" title="see questions tagged &#39;osmchange&#39;">osmchange</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Feb '21, 13:02</strong></p>
<img src="https://secure.gravatar.com/avatar/d147b24e965b097c77da7e289ce183f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Saaj&#39;s gravatar image" />
<p><span>Saaj</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Saaj has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78663" class="comments-container">
<span id="78672"></span>
<div id="comment-78672" class="comment">
<div id="post-78672-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. The problem is we have taxi dispatch software that uses the OSRM server so this change needs to be here so that our software automatically picks up this route.</p>
<p>Someone advised the following: "Maybe put a motor_vehicle=no tag and a note describing this situation?"</p>
<p>Can you advise how to do this?#</p>
<p>Saaj</p>
</div>
<div id="comment-78672-info" class="comment-info">
<span class="comment-age">(05 Feb '21, 09:53)</span> <span class="comment-user userinfo">Saaj</span>
</div>
</div>
<span id="78674"></span>
<div id="comment-78674" class="comment">
<div id="post-78674-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><code>motor_vehicle=no</code> only goes on a node if there actually is a legal or physical restriction for motor vehicles to pass. Don't use it to convey your personal routing preferences.</p>
</div>
<div id="comment-78674-info" class="comment-info">
<span class="comment-age">(05 Feb '21, 10:18)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="78681"></span>
<div id="comment-78681" class="comment">
<div id="post-78681-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The osrm server runs on donated hardware and is supported by volunteers like me. Using it commercially as a backend for a taxi dispatch software is not acceptable. Acceptable commercial usage is limited to non-essential services, like providing a route for customers to the shop as part of a shop website. For a taxi dispatch, I would deem routing an essential service. The full usage policy can be found at <a href="https://www.fossgis.de/arbeitsgruppen/osm-server/nutzungsbedingungen/">https://www.fossgis.de/arbeitsgruppen/osm-server/nutzungsbedingungen/</a></p>
</div>
<div id="comment-78681-info" class="comment-info">
<span class="comment-age">(05 Feb '21, 17:24)</span> <span class="comment-user userinfo">datendelphin</span>
</div>
</div>
</div>
<div id="comment-tools-78663" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78663-form-container" class="comment-form-container">
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

<span id="78664"></span>

<div id="answer-container-78664" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78664-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78664-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-78664-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The routing is provided by external providers (respectively FOSSGIS &amp; Graphhopper) so it is best to report the issue to them.</p>
<p>At present I cannot see any specific information on OSM which causes this other than differences in route length (i.e., there do not seem to be any breaks in the routing graph for the A75): the two routes toggle just S of Panure Bridge with a route length of around 71 km.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Feb '21, 13:14</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-78664" class="comments-container">
&#10;</div>
<div id="comment-tools-78664" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78664-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78665"></span>

<div id="answer-container-78665" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78665-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78665-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78665-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are other OSM based routers out there where you can finetune more. Check out <a href="https://maps.openrouteservice.org/directions?n1=54.578365&amp;n2=-3.892608&amp;n3=9&amp;a=55.064297,-3.642328,54.9157,-3.987941,54.882924,-4.973993&amp;b=0&amp;c=0&amp;k1=en-US&amp;k2=km">OpenRouteService</a> for example where you can define intermediate points to tweak the route.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Feb '21, 13:33</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-78665" class="comments-container">
&#10;</div>
<div id="comment-tools-78665" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78665-form-container" class="comment-form-container">
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

