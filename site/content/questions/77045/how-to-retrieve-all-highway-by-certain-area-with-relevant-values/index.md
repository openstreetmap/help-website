+++
type = "question"
title = "How To Retrieve All Highway By Certain Area With Relevant Values?"
description = '''Hello Guys I&#x27;m Newcomer Here. Recently I Have A Project Want To Use OSM With Overpass API. My Requirements Are:   Retrieve All Streets (Highway) In A Specified Area. I Know This Is Possible By Kinds Of Ways. For Example Set Query Type As Boundary And Boundary Type = Admin Then Admin Level = N Or By ...'''
date = "2020-10-12T05:29:00Z"
lastmod = "2020-10-19T13:27:00Z"
weight = 77045
keywords = [ "overpass", "nodes", "roadtype", "way", "highway" ]
aliases = [ "/questions/77045" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How To Retrieve All Highway By Certain Area With Relevant Values?](/questions/77045/how-to-retrieve-all-highway-by-certain-area-with-relevant-values)

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
<span id="post-77045-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77045-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77045-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello Guys</p>
<p>I'm Newcomer Here. Recently I Have A Project Want To Use OSM With Overpass API. My Requirements Are:</p>
<ol>
<li><p>Retrieve All Streets (Highway) In A Specified Area. I Know This Is Possible By Kinds Of Ways. For Example Set Query Type As Boundary And Boundary Type = Admin Then Admin Level = N Or By Area With Area ID (Relation ID).</p></li>
<li><p>I Need To Get A Lists Of All Highways With Way Type (For Example Motorway / Trunk / Primary / Secondary / Tertiar) And Availability Of Driving And Direction (For Example Is That Way A West-Eastward Way &lt;horizontal&gt; Or North-Southward Way &lt;vertical&gt;. My Question Is That Possible To List All Roads With All Required Values?</p></li>
<li>I Also Need All Corresponding Nodes (Longitude / Latitude) In A Road (Highway). Does Overpass API Support To Get Nodes Relation Of A Highway? If I Need Only A Few Nodes In A Way Can I Set Parameter (Meter) As Wanted Distance Between Nodes (For Example Every N Meter For A Node)?</li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-roadtype" rel="tag" title="see questions tagged &#39;roadtype&#39;">roadtype</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Oct '20, 05:29</strong></p>
<img src="https://secure.gravatar.com/avatar/1adad0f5c60437256d24d3b9975b287b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bright&#39;s gravatar image" />
<p><span>Bright</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bright has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77045" class="comments-container">
<span id="77049"></span>
<div id="comment-77049" class="comment">
<div id="post-77049-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It sounds like you have half of it. Have you written any code a a basis?</p>
</div>
<div id="comment-77049-info" class="comment-info">
<span class="comment-age">(12 Oct '20, 16:25)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-77045" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77045-form-container" class="comment-form-container">
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

<span id="77152"></span>

<div id="answer-container-77152" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77152-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77152-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-77152-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Amended VIPINDAS K's answer so it runs. Pivot converts an area into an element. ^ and $ are part of regular expressions, defining the begining &amp; ending of a string. In this example it searches for highways the are either 'trunk' or 'primary'. 'trunk_link' would not be returned,</p>
<pre><code>{{geocodeArea:Malappuram}};
rel(pivot)-&gt;.District;
wr[highway~&quot;^(trunk|primary)$&quot;](area);
out geom; 
.District out geom;
&#10;{{style: 
way{
color: green;
fill-color: green;
text: name:en;
}
relation{
color: green;
fill-color: green;
text: name:en;
}
}}</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '20, 13:27</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-77152" class="comments-container">
&#10;</div>
<div id="comment-tools-77152" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77152-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="77145"></span>

<div id="answer-container-77145" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77145-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77145-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77145-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sample code:<br />
[out:json][timeout:25];<br />
// fetch area “Malappuram" to search in<br />
{{geocodeArea:Malappuram}}-&gt;.searchArea;<br />
// gather results<br />
(<br />
//query part for: “boundary=Malappuram”;<br />
wr["boundary"="administrative"]["name"="Malappuram"]["admin_level"="5"](area.searchArea);<br />
way["highway"="trunk"](area.searchArea);<br />
way["highway"="primary"](area.searchArea);<br />
relation["highway"="trunk"](area.searchArea);<br />
relation["highway"="primary"](area.searchArea);<br />
//we can add more tags<br />
way{<br />
color: green;<br />
fill-color: green;<br />
text: name:en;<br />
}<br />
relation{<br />
color: green;<br />
fill-color: green;<br />
text: name:en;<br />
}<br />
);<br />
// print results<br />
out body;<br />
&gt;;<br />
out skel qt;<br />
<br />
wizard helps to create codes.<br />
Qgis helps to make customized map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '20, 08:49</strong></p>
<img src="https://secure.gravatar.com/avatar/fc9c2a007c6f81684415bb1f16f2991c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VIPINDAS%20K&#39;s gravatar image" />
<p><span>VIPINDAS K</span><br />
<span class="score" title="125 reputation points">125</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VIPINDAS K has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Oct '20, 08:59</strong> </span></p>
</div>
</div>
<div id="comments-container-77145" class="comments-container">
&#10;</div>
<div id="comment-tools-77145" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77145-form-container" class="comment-form-container">
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

