+++
type = "question"
title = "OSRM directions through roundabout- bug or tagging error?"
description = '''I&#x27;ve noticed sometimes the OSRM router gives odd directions through a roundabout. Is this a bug in the router, or is there something wrong with the tagging? For example, here, the directions are to &quot;take the exit onto WA14&quot;, rather than to &quot;take the second exit onto Washougal River Road&quot;. And again ...'''
date = "2019-08-30T22:33:00Z"
lastmod = "2019-09-17T10:39:00Z"
weight = 70572
keywords = [ "directions", "osrm", "roundabout", "tagging" ]
aliases = [ "/questions/70572" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [OSRM directions through roundabout- bug or tagging error?](/questions/70572/osrm-directions-through-roundabout-bug-or-tagging-error)

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
<span id="post-70572-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70572-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70572-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've noticed sometimes the OSRM router gives odd directions through a roundabout. Is this a bug in the router, or is there something wrong with the tagging?</p>
<p><a href="https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&amp;route=45.57619%2C-122.35607%3B45.57761%2C-122.35584#map=18/45.57691/-122.35606">For example, here,</a> the directions are to "take the exit onto WA14", rather than to "take the second exit onto Washougal River Road". <a href="https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&amp;route=45.57705%2C-122.35763%3B45.57763%2C-122.35577">And again here</a>, same error for a different starting point. <a href="https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&amp;route=45.57627%2C-122.35488%3B45.57692%2C-122.35724">But this route</a> recognizes the first exit and counts it.</p>
<p><a href="https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&amp;route=45.57447%2C-122.33888%3B45.57326%2C-122.33694">Similarly at this nearby roundabout</a>, all three routes exiting to the South give bad directions, while the routes exiting north are described as expected.</p>
<p>Is this something I've tagged wrongly? I can't see any difference between the ones that work and the ones that don't.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-directions" rel="tag" title="see questions tagged &#39;directions&#39;">directions</span> <span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-roundabout" rel="tag" title="see questions tagged &#39;roundabout&#39;">roundabout</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Aug '19, 22:33</strong></p>
<img src="https://secure.gravatar.com/avatar/135acfe781ee8e2806a04e60d8e2b1c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="noliver&#39;s gravatar image" />
<p><span>noliver</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="noliver has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Aug '19, 22:35</strong> </span></p>
</div>
</div>
<div id="comments-container-70572" class="comments-container">
<span id="70812"></span>
<div id="comment-70812" class="comment">
<div id="post-70812-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think the first two examples don't count the first exit as the roundabout section as the same name as the lead in road and OSRM believes to be on the same road so does not count it. I am not sure if roundabouts should have the road name. What if two major roads met at a roundabout, what name would you give to the roundabout? the first or the second?</p>
</div>
<div id="comment-70812-info" class="comment-info">
<span class="comment-age">(16 Sep '19, 23:30)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="70818"></span>
<div id="comment-70818" class="comment">
<div id="post-70818-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It does seem likely that some router packages may be confused by the circular ring having the name of one of the streets, as andy mackey suggested. The wiki page for the junction=roundabout tag <a href="https://wiki.openstreetmap.org/wiki/Tag:junction%3Droundabout#How_to_map">https://wiki.openstreetmap.org/wiki/Tag:junction%3Droundabout#How_to_map</a> says this about naming:</p>
<p>"Give it a name only if is official or displayed (generally it is different from the name of highways connecting or passing though them, but many of them remain unnamed as it is undecidable between these competing highways, and because there's no address for residents located inside, or because addresses are given to one of the connecting highways: only large roundabouts have a dedicated name)."</p>
<p>and this:</p>
<p>"Again, a roundabout should only be tagged with name=* if the junction itself is named independently and differently from the roads crossing it."</p>
</div>
<div id="comment-70818-info" class="comment-info">
<span class="comment-age">(17 Sep '19, 10:39)</span> <span class="comment-user userinfo">yesimlost</span>
</div>
</div>
</div>
<div id="comment-tools-70572" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70572-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="70609"></span>

<div id="answer-container-70609" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70609-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70609-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-70609-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't think there is anything wrong with the data. Looking at the tags I don't see anything out of the usual and there are other routers that generate correct turn by turn instructions, even other OSRM instances. There must be something wrong with the OSRM implementation used here. You could open a ticket on <a href="https://github.com/Project-OSRM">Github</a> to address the issue there.</p>
<p>These are working fine for example:<br />
<a href="https://map.project-osrm.org/?z=17&amp;center=45.575660%2C-122.355493&amp;loc=45.576171%2C-122.356035&amp;loc=45.577381%2C-122.355814&amp;hl=en&amp;alt=0">map.project-osm.org</a><br />
<a href="https://www.openstreetmap.org/directions?engine=graphhopper_car&amp;route=45.57619%2C-122.35607%3B45.57761%2C-122.35584">Graphhopper on openstreetmap.org</a></p>
<p><a href="https://routing.openstreetmap.de/?z=18&amp;center=45.576794%2C-122.356059&amp;loc=45.576156%2C-122.356088&amp;loc=45.577381%2C-122.355814&amp;hl=de&amp;alt=0&amp;srv=0">OSRM on openstreetmap.de</a> is doing it wrong again.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Sep '19, 10:04</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span> </br></br></p>
</div>
</div>
<div id="comments-container-70609" class="comments-container">
<span id="70815"></span>
<div id="comment-70815" class="comment">
<div id="post-70815-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. I've done some more research and opened an issue here: <a href="https://github.com/Project-OSRM/osrm-backend/issues/5554">https://github.com/Project-OSRM/osrm-backend/issues/5554</a></p>
</div>
<div id="comment-70815-info" class="comment-info">
<span class="comment-age">(17 Sep '19, 03:10)</span> <span class="comment-user userinfo">noliver</span>
</div>
</div>
</div>
<div id="comment-tools-70609" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70609-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="70816"></span>

<div id="answer-container-70816" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70816-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70816-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-70816-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When you switch the router to Graphhopper, you will notice that that router numbers the exits. So there is nothing wrong with the data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Sep '19, 05:41</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-70816" class="comments-container">
&#10;</div>
<div id="comment-tools-70816" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70816-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="70601"></span>

<div id="answer-container-70601" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70601-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70601-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70601-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have looked at the data and the one way sections into and out of the roundabouts have turn restrictions which i don't think are needed, oneway on the road should do the job. They may be the problem. I also think giving the roundabout the name of the road may be causing a problem OSRM may use logic that assumes the roundabout as a continuation of the road so doesn't count it, and therefore second exit is reduced to the first, maybe? This one in Peterborough UK ( we drive on the wrong side here) works in the 3rd exit type description. and does not have the turn restrictions mapped, or naming issue. It just as one way on the one way sections. <a href="https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&amp;route=52.6011%2C-0.2081%3B52.5981%2C-0.2147">https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&amp;route=52.6011%2C-0.2081%3B52.5981%2C-0.2147</a> I don't think OSRM directions are good either, They are confusing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Sep '19, 17:22</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Sep '19, 23:38</strong> </span></p>
</div>
</div>
<div id="comments-container-70601" class="comments-container">
<span id="70610"></span>
<div id="comment-70610" class="comment">
<div id="post-70610-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The only turn restrictions I see are forbidding u-turns where the carriageways split into entry and exit ramps (unless someone edited anything in the meantime). I don't think they should influence the instructions for leaving the roundabout.</p>
</div>
<div id="comment-70610-info" class="comment-info">
<span class="comment-age">(03 Sep '19, 10:07)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="70810"></span>
<div id="comment-70810" class="comment">
<div id="post-70810-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Her's one of the turn restrictions, in my opinion the one way section means the turn restrictions are not needed. <a href="https://www.openstreetmap.org/node/6742527237">https://www.openstreetmap.org/node/6742527237</a></p>
</div>
<div id="comment-70810-info" class="comment-info">
<span class="comment-age">(16 Sep '19, 23:10)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="70814"></span>
<div id="comment-70814" class="comment">
<div id="post-70814-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I see what you mean--I wouldn't have created those manually in JOSM, but the ID turn restriction editor sort of implies that this restriction may be desirable, since without them, it shows a possible u-turn from the two-way street back onto itself instead of continuing on to the one-way portion. I think it's unlikely any router would try to use that route with the roundabout just ahead, so you're probably right that they're unnecessary, and I won't make a habit of creating them, and may come back and remove them once this issue is resolved.</p>
<p>In this specific case, they are not present at the adjacent roundabout where OSRM also has issues, so I don't think they're the root of this issue.</p>
</div>
<div id="comment-70814-info" class="comment-info">
<span class="comment-age">(17 Sep '19, 03:08)</span> <span class="comment-user userinfo">noliver</span>
</div>
</div>
</div>
<div id="comment-tools-70601" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70601-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="70807"></span>

<div id="answer-container-70807" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70807-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Looking at satellite images for the intersections mentioned by the original poster, these look like ordinary four-way crossings, not roundabouts. Were these recently redone as roundabouts?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Sep '19, 21:27</strong></p>
<img src="https://secure.gravatar.com/avatar/18cebb6e015be089dffe6e41768bdf3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yesimlost&#39;s gravatar image" />
<p><span>yesimlost</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yesimlost has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70807" class="comments-container">
<span id="70811"></span>
<div id="comment-70811" class="comment">
<div id="post-70811-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The mapper (noliver) does say, in the edit, new roundabout.</p>
</div>
<div id="comment-70811-info" class="comment-info">
<span class="comment-age">(16 Sep '19, 23:13)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="70813"></span>
<div id="comment-70813" class="comment">
<div id="post-70813-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Yes, these were both installed in the last 3 months, the first in early July.</p>
</div>
<div id="comment-70813-info" class="comment-info">
<span class="comment-age">(17 Sep '19, 01:06)</span> <span class="comment-user userinfo">noliver</span>
</div>
</div>
</div>
<div id="comment-tools-70807" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70807-form-container" class="comment-form-container">
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

