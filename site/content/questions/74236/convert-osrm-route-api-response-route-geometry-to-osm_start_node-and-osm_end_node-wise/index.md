+++
type = "question"
title = "Convert osrm route api response (route geometry) to osm_start_node and osm_end_node wise."
description = '''I am using osrm for route api. The response i got from osrm route is geometry and nodes. I want to slit the line-string to response given below. Desired example of response: [{&quot;type&quot;:&quot;Feature&quot;,&quot;geometry&quot;: {&quot;type&quot;:&quot;LineString&quot;,&quot;coordinates&quot;:[  [73.08365, 33.662523],  [73.083333, 33.662344],  [73.0830...'''
date = "2020-04-17T07:18:00Z"
lastmod = "2020-04-17T13:24:00Z"
weight = 74236
keywords = [ "osmendnode", "osrm", "javascript", "osm", "osmstartnode" ]
aliases = [ "/questions/74236" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Convert osrm route api response (route geometry) to osm_start_node and osm_end_node wise.](/questions/74236/convert-osrm-route-api-response-route-geometry-to-osm_start_node-and-osm_end_node-wise)

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
<span id="post-74236-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74236-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74236-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using osrm for route api. The response i got from osrm route is geometry and nodes. I want to slit the line-string to response given below.</p>
<p><strong>Desired example of response:</strong></p>
<pre><code>[{&quot;type&quot;:&quot;Feature&quot;,&quot;geometry&quot;:
{&quot;type&quot;:&quot;LineString&quot;,&quot;coordinates&quot;:[
    [73.08365, 33.662523],
    [73.083333, 33.662344],
    [73.083071, 33.662188],
    [73.082894, 33.662081],
    [73.082701, 33.661965],
    [73.08239, 33.661795],
    [73.082159, 33.661643],
    [73.081923, 33.661474],
    [73.081135, 33.660951],
    [73.080701, 33.660661],
    [73.08046, 33.660509],
    [73.080272, 33.660384],
    [73.08002, 33.660224],
    [73.079741, 33.660072],
    [73.079371, 33.659875],
    [73.078969, 33.659648],
    [73.078336, 33.659313],
    [73.077741, 33.659],
   ]},
properties:
{&quot;osmhighway&quot;:&quot;motorway_link&quot;,&quot;osmoneway&quot;:&quot;yes&quot;,&quot;osmwayid&quot;:5669636,&quot;start_node&quot;:370705004,&quot;end_node&quot;:1369956654,
&quot;speed_mean_mph&quot;:16,&quot;pct_from_freeflow&quot;:72,&quot;speed_freeflow_mph&quot;:22}},{&quot;type&quot;:&quot;Feature&quot;,&quot;geometry&quot;:
{&quot;type&quot;:&quot;LineString&quot;,&quot;coordinates&quot;:[
&#10;    [73.077741, 33.659],
    [73.077194, 33.658714],
    [73.076765, 33.658496],
    [73.076508, 33.658344],
    [73.075672, 33.65792],
    [73.075012, 33.657576],
    [73.074465, 33.657295],
    [73.073929, 33.657031],
    [73.073023, 33.656571],
    [73.072438, 33.656281],
    [73.071983, 33.65604],
    [73.071457, 33.655763],
    [73.071044, 33.65554],
    [73.070401, 33.655196],
    [73.069993, 33.654959],
    [73.069511, 33.654723],
    [73.069136, 33.654535],
    [73.067977, 33.653959],
    [73.06742, 33.653669],
    [73.066894, 33.653401],
    [73.066487, 33.653204],
    [73.065948, 33.652923],
    [73.06547, 33.652668],
    [73.065084, 33.652463],
    [73.064677, 33.652262],
    [73.063941, 33.65186],
    [73.063378, 33.651552],
    [73.062907, 33.651307]]},
properties:
{&quot;osmhighway&quot;:&quot;motorway_link&quot;,&quot;osmoneway&quot;:&quot;yes&quot;,&quot;osmwayid&quot;:5669636,&quot;start_node&quot;:42469049,&quot;end_node&quot;:1369956654,
&quot;speed_mean_mph&quot;:16,&quot;pct_from_freeflow&quot;:72,&quot;speed_freeflow_mph&quot;:22}},
{&quot;type&quot;:&quot;Feature&quot;,&quot;geometry&quot;:{&quot;type&quot;:&quot;LineString&quot;,&quot;coordinates&quot;:
[[73.064677, 33.652262],
[73.063941, 33.65186],
[73.063378, 33.651552],
[73.062907, 33.651307],
[73.062354, 33.650985],
[73.061856, 33.650713],
[73.061486, 33.650512],
[73.060987, 33.650244],
[73.060424, 33.649949],
[73.059218, 33.649297],
[73.057212, 33.64827],
[73.056328, 33.647792]
]},
properties:{&quot;osmname&quot;:&quot;Bay Parkway&quot;,&quot;osmhighway&quot;:&quot;primary&quot;,&quot;osmoneway&quot;:&quot;no&quot;,&quot;osmwayid&quot;:5675398,&quot;start_node&quot;:36202597,
&quot;end_node&quot;:36202835,&quot;speed_mean_mph&quot;:20,&quot;pct_from_freeflow&quot;:67,&quot;speed_freeflow_mph&quot;:29}}]</code></pre>
<p>But the response i got from osrm route api is given below.</p>
<p><strong>osrm route api response:</strong></p>
<pre><code>{&quot;routes&quot;:[{&quot;geometry&quot;:{&quot;coordinates&quot;:[[13.388798,52.517033],[13.388827,52.516848],[13.389003,52.516864],[13.389842,52.51692],[13.390517,52.516965],[13.390708,52.516983],[13.39089,52.517003],[13.392584,52.517118],[13.393055,52.517149],[13.393172,52.517192],[13.39314,52.517372],[13.393103,52.517377],[13.393052,52.517385],[13.39296,52.517399],[13.392852,52.5174],[13.392628,52.517386],[13.392347,52.519016],[13.392296,52.519063],[13.392249,52.519105],[13.392231,52.519122],[13.392225,52.519131],[13.392173,52.519237],[13.391997,52.52006],[13.39199,52.520089],[13.391985,52.520111],[13.391949,52.520261],[13.391931,52.520348],[13.391886,52.520573],[13.39185,52.520768],[13.391838,52.520829],[13.391629,52.521964],[13.391643,52.522074],[13.391649,52.522156],[13.391676,52.522717],[13.391704,52.522807],[13.391718,52.522858],[13.391782,52.522976],[13.392118,52.523552],[13.392549,52.524365],[13.392789,52.524807],[13.392821,52.524865],[13.392884,52.524984],[13.392948,52.525096],[13.392967,52.525131],[13.393075,52.525323],[13.393195,52.525538],[13.393295,52.52564],[13.393344,52.525736],[13.393387,52.525821],[13.393407,52.52588],[13.393407,52.525992],[13.393586,52.526289],[13.393565,52.52634],[13.393541,52.526401],[13.393492,52.526483],[13.392896,52.527482],[13.392668,52.527848],[13.392638,52.527894],[13.392528,52.52806],[13.392498,52.52811],[13.392425,52.528233],[13.392659,52.528281],[13.392712,52.528292],[13.39314,52.528379],[13.393219,52.528396],[13.393668,52.528491],[13.393814,52.528526],[13.393989,52.52857],[13.394591,52.528715],[13.395724,52.528996],[13.397265,52.529357],[13.397326,52.529372],[13.397565,52.529429],[13.397631,52.529432]],&quot;type&quot;:&quot;LineString&quot;},&quot;legs&quot;:[{&quot;annotation&quot;:{&quot;nodes&quot;:[21487242,2264199819,6583929461,3869306771,6583929470,25664779,6583929468,450169274,3602294176,29207420,1263312256,262455378,7026359390,7026359391,262455379,27005148,3378459473,4590472037,4590472043,25665679,4590472042,3378459484,29192960,3590535063,1635318723,1635318763,3463843411,3463843421,540972281,4843707050,539817446,27412113,541130319,3463843610,3463843613,2435547302,27412088,27412072,29192284,2489942693,2344513388,26871464,2344513396,2435547308,5426423331,672892368,1769645439,1769645505,1769645476,2341815347,1769645437,2269947166,5700339361,25954549,5700339360,1448679340,3185200556,6665554019,5700389945,5700389948,311464976,5700389949,5700389946,3933855818,3185200558,4815315420,26871576,4815315421,3933855819,1448679343,5700389941,3836987623,659394041,3836987625]},&quot;summary&quot;:&quot;&quot;,&quot;weight&quot;:618.2,&quot;duration&quot;:408.5,&quot;steps&quot;:[],&quot;distance&quot;:1998.6}],&quot;weight_name&quot;:&quot;routability&quot;,&quot;weight&quot;:618.2,&quot;duration&quot;:408.5,&quot;distance&quot;:1998.6}],&quot;waypoints&quot;:[{&quot;distance&quot;:4.231665624816857,&quot;name&quot;:&quot;Friedrichstraße&quot;,&quot;location&quot;:[13.388798,52.517033]},{&quot;distance&quot;:2.7893928415656375,&quot;name&quot;:&quot;Torstraße&quot;,&quot;location&quot;:[13.397631,52.529432]}],&quot;code&quot;:&quot;Ok&quot;}</code></pre>
<p>Now i want to create response like above mentioned example.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmendnode" rel="tag" title="see questions tagged &#39;osmendnode&#39;">osmendnode</span> <span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osmstartnode" rel="tag" title="see questions tagged &#39;osmstartnode&#39;">osmstartnode</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Apr '20, 07:18</strong></p>
<img src="https://secure.gravatar.com/avatar/7bcb30fb8dd1a5405cafc2ef9fad42bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ahsan368&#39;s gravatar image" />
<p><span>ahsan368</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ahsan368 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Apr '20, 09:20</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-74236" class="comments-container">
<span id="74241"></span>
<div id="comment-74241" class="comment">
<div id="post-74241-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>cross-post: <a href="https://gis.stackexchange.com/questions/358620/convert-osrm-geometry-linestring-to-osm-startnode-and-endnode-wise">https://gis.stackexchange.com/questions/358620/convert-osrm-geometry-linestring-to-osm-startnode-and-endnode-wise</a></p>
</div>
<div id="comment-74241-info" class="comment-info">
<span class="comment-age">(17 Apr '20, 13:24)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-74236" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74236-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

