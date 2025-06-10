+++
type = "question"
title = "Get next X adjacent ways from current way"
description = '''Hi First let me say that I am fairy new to OSM and the Overpass api. So forgive my ignorance ;)  I&#x27;m working on a small private app where I want to get information about the road I am currently driving on. I am using the following query to get information about the road from the phones current locat...'''
date = "2013-09-28T21:13:00Z"
lastmod = "2014-04-21T11:50:00Z"
weight = 26832
keywords = [ "overpassapi", "overpass", "ways" ]
aliases = [ "/questions/26832" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Get next X adjacent ways from current way](/questions/26832/get-next-x-adjacent-ways-from-current-way)

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
<span id="post-26832-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26832-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26832-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>First let me say that I am fairy new to OSM and the Overpass api. So forgive my ignorance ;)</p>
<p>I'm working on a small private app where I want to get information about the road I am currently driving on. I am using the following query to get information about the road from the phones current location:</p>
<pre><code>&lt; osm-script&gt;
    &lt; query type=&quot;way&quot;&gt;
        &lt; around lat=&quot;56.09383&quot; lon=&quot;9.00309&quot; radius=&quot;5&quot;/&gt;
        &lt; has-kv k=&quot;highway&quot;/&gt;
    &lt; /query&gt;
    &lt; union&gt;
        &lt; item /&gt;
        &lt; recurse type=&quot;way-node&quot;/&gt;
    &lt; /union&gt;
    &lt; print order=&quot;quadtile&quot;/&gt;
&lt; /osm-script&gt;</code></pre>
<p>In the example above i get the way: "Midtjyske Motorvej" with ID=111435507 I am not sure if this is the best way to do it, but it seems to work quite good for now.</p>
<p>Because I do not want to query Overpass every single second, but still want the information to be rather accurate, I thought about trying to make the app make an educated guess about where I'm heading, and then cache some of this information locally.</p>
<p>So I want the app to query via the overpass API, and then find for example the next 10 adjacent ways (or the next x adjacent ways within a 2 KM radius) of the current way i'm driving on. If for instance I was driving south on the above road: "<a href="http://www.openstreetmap.org/browse/way/111435507">111435507</a>", the immediate next adjacent way would be: "<a href="http://www.openstreetmap.org/browse/way/111435449">111435449</a>", the next one would be: "<a href="http://www.openstreetmap.org/browse/way/111435478">111435478</a>" etc. Is it possible to create one query that can get all the adjacent ways like this?</p>
<p>I don't expect the API to handle direction/course, so I guess I will have to do that calculation my self, and figure out which end point of the way I want to start from - so to speak. But if it is possible, that would of course be great :)</p>
<p>Thanx in advance!</p>
<p>...Allan</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Sep '13, 21:13</strong></p>
<img src="https://secure.gravatar.com/avatar/3eee8e523c27678a115c28127e5bad64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="as_dk&#39;s gravatar image" />
<p><span>as_dk</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="as_dk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26832" class="comments-container">
&#10;</div>
<div id="comment-tools-26832" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26832-form-container" class="comment-form-container">
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

<span id="32489"></span>

<div id="answer-container-32489" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32489-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32489-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-32489-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Although it looks a bit weird this will give you the next 5 adjacent roads for way id 111435507.</p>
<pre><code>[bbox:{{bbox}}];
way(111435507);
(way(around:0)[highway~&quot;.&quot;][highway!~&quot;path|track|cycleway|footway&quot;];(._;&gt;;))-&gt;.a;
(way(around:0)[highway~&quot;.&quot;][highway!~&quot;path|track|cycleway|footway&quot;];(._;&gt;;))-&gt;.b;
(way(around:0)[highway~&quot;.&quot;][highway!~&quot;path|track|cycleway|footway&quot;];(._;&gt;;))-&gt;.c;
(way(around:0)[highway~&quot;.&quot;][highway!~&quot;path|track|cycleway|footway&quot;];(._;&gt;;))-&gt;.d;
(way(around:0)[highway~&quot;.&quot;][highway!~&quot;path|track|cycleway|footway&quot;];(._;&gt;;))-&gt;.e;
(.a;.b;.c;.d;.e;);out;</code></pre>
<p>Try it on <a href="http://overpass-turbo.eu/s/3ap">Overpass Turbo</a></p>
<p>Note that "around" has no concept of directly connected roads, so you will get some roads which are only crossing the motorway. You will have to manually filter those out in a post processing step.</p>
<p>Edit: Global bbox added to restrict your search to the area you're interested in. Otherwise really long ways will cause some far away data to be fetched.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Apr '14, 11:50</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Apr '14, 18:16</strong> </span></p>
</div>
</div>
<div id="comments-container-32489" class="comments-container">
&#10;</div>
<div id="comment-tools-32489" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32489-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="26866"></span>

<div id="answer-container-26866" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26866-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26866-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26866-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Silly question : the radius is one parameter in your current query (expressed in meters). Why simply not change this 'radius' from '5' to '2000' ?</p>
<p>Then you will retrieve all highways within the circle. Then you will have to build a function retrieving the nearest highway from the current phone position (this will depend how you store the geodata in your app but they are plenty of geo-libs doing this for you).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Sep '13, 14:32</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-26866" class="comments-container">
<span id="26892"></span>
<div id="comment-26892" class="comment">
<div id="post-26892-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the answer :)</p>
<p>I have of course already tried that and it also works fine. But I really want the response data to be as minimal as possible and only return what I need in order to save bandwidth on the mobile device. With a radius of 2km I get about 200Kb at the location in the previous message. Upping that to 5km gives 1Mb – still semi ok I guess. But in a bigger city like (55.703956,12.518066) I get 1Mb of data for only 2 km and 7mb with 5 Km. A lot of data when I know I will only need a small part of that in the current request.</p>
</div>
<div id="comment-26892-info" class="comment-info">
<span class="comment-age">(01 Oct '13, 16:04)</span> <span class="comment-user userinfo">as_dk</span>
</div>
</div>
<span id="26893"></span>
<div id="comment-26893" class="comment">
<div id="post-26893-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I really only want to get connecting (better word perhaps than adjacent ways I guess) ways, and nothing else. And preferably only ways at the endnodes, so I don’t get side roads etc.</p>
<p>I’m sorry I did not make that clear in my question.</p>
</div>
<div id="comment-26893-info" class="comment-info">
<span class="comment-age">(01 Oct '13, 16:04)</span> <span class="comment-user userinfo">as_dk</span>
</div>
</div>
<span id="26894"></span>
<div id="comment-26894" class="comment">
<div id="post-26894-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can edit and improve your question at any time. I'm surprised by the size of the data. Perhaps the radius should vary with the speed. In urban and dense areas, the speed is necessarily smaller than in country side.</p>
</div>
<div id="comment-26894-info" class="comment-info">
<span class="comment-age">(01 Oct '13, 16:36)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-26866" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26866-form-container" class="comment-form-container">
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

