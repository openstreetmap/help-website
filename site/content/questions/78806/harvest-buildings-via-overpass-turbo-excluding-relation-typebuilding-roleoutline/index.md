+++
type = "question"
title = "Harvest buildings - via overpass turbo - excluding relation type:building; role:outline"
description = '''Hi, I am attempting to harvest buildings via overpass turbo. I want all buildings excluding buildings with relation type=building role=outline. i.e.: When buildings are composed of parts I only want the parts and not the outline and all other buildings. The first attempt; [out:json][timeout:25]; are...'''
date = "2021-02-11T16:16:00Z"
lastmod = "2021-02-17T19:56:00Z"
weight = 78806
keywords = [ "building", "overpass-turbo", "relation" ]
aliases = [ "/questions/78806" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Harvest buildings - via overpass turbo - excluding relation type:building; role:outline](/questions/78806/harvest-buildings-via-overpass-turbo-excluding-relation-typebuilding-roleoutline)

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
<span id="post-78806-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78806-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78806-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am attempting to harvest buildings via overpass turbo. I want all buildings <em>excluding</em> buildings with relation <code>type=building</code> <code>role=outline</code>. i.e.: When buildings are composed of parts I only want the parts and not the outline and all other buildings. The first attempt;</p>
<pre><code>[out:json][timeout:25];
area[name=&#39;Chapel Street Primary School&#39;];
relation[&quot;type&quot;=&quot;building&quot;](area) -&gt; .relation;
(way(r.relation)[&quot;building&quot;]; -
way(r.relation:!&quot;outline&quot;););
/*added by auto repair*/
(._;&gt;;);
/*end of auto repair*/
out qt;</code></pre>
<p>returns the parts and correctly excludes the building outline but unfortunately all other buildings. The second attempt;</p>
<pre><code>[out:json][timeout:25];
(area[name=&quot;Chapel Street Primary School&quot;];
 way[&quot;building&quot;!=&quot;outline&quot;](area);
 //relation[&quot;building&quot;!=&quot;outline&quot;](area); 
);
out body;
&gt;;
out skel qt;</code></pre>
<p>includes the <em>normal</em> buildings, the <code>building:parts</code> and only seemingly excludes the building outline ~ I can't select it in the overpass turbo Map ~ its still in the Data though. How can I execute this query successfully?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Feb '21, 16:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a235da08f7d6877654b16dfe832aed66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arkriger&#39;s gravatar image" />
<p><span>arkriger</span><br />
<span class="score" title="155 reputation points">155</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arkriger has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Feb '21, 19:26</strong> </span></p>
</div>
</div>
<div id="comments-container-78806" class="comments-container">
<span id="78810"></span>
<div id="comment-78810" class="comment">
<div id="post-78810-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think building relations are fairly rare compared with simply marking the outline as <code>building=*</code> and the parts as <code>building:part=*</code> and letting the consumer figure out which parts belong to which building. TagInfo lists all building relations as having 194 487 members in total, while <code>building:part</code> alone has 1 698 253 uses (which would exclude <code>outline</code> ways).</p>
</div>
<div id="comment-78810-info" class="comment-info">
<span class="comment-age">(12 Feb '21, 02:59)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="78813"></span>
<div id="comment-78813" class="comment">
<div id="post-78813-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. I understand building relations a bit clearer now.<br />
How do I harvest building:part and <em>normal</em> building while excluding outlines when building:part exists? How would I do this in a single query?</p>
</div>
<div id="comment-78813-info" class="comment-info">
<span class="comment-age">(12 Feb '21, 11:19)</span> <span class="comment-user userinfo">arkriger</span>
</div>
</div>
<span id="78815"></span>
<div id="comment-78815" class="comment">
<div id="post-78815-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unfortunately, I'm not able to offer much constructive there. My first thought is to try to exclude the amalgamated <code>building:part</code> areas from the search area, but that doesn't actually sound very efficient to me as it involves lots of 'temp' geometry. While I have dabbled in overpass over the years, I have generally stuck to rather simple queries.</p>
</div>
<div id="comment-78815-info" class="comment-info">
<span class="comment-age">(12 Feb '21, 12:40)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-78806" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78806-form-container" class="comment-form-container">
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

<span id="78836"></span>

<div id="answer-container-78836" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78836-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78836-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78836-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="arkriger has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try this one:</p>
<pre><code>[out:json][timeout:25];
area[name=&#39;Chapel Street Primary School&#39;]-&gt;.a;
&#10;(
  (
    // I want all buildings
    way[building](area.a);
&#10;    // plus every building:part
    way[&quot;building:part&quot;](area.a);
  );
-
  // excluding buildings with relation type=building role=outline
  (
    // for every way in the input set select the relations of which it is an &quot;outline&quot; member
    rel(bw:&quot;outline&quot;);
    // back to the ways with role &quot;outline&quot;
    way(r:&quot;outline&quot;);
  );
);
&#10;out body;
&gt;;
out skel qt;</code></pre>
<p>It is probably not much efficient, so I think <strong>if</strong> it works, it does only for very small areas.</p>
<p>Please notice:</p>
<ul>
<li>'Chapel Street Primary School' identifies multiple places; you should use '{{bbox}}' or 'area(id:2432441915)' (24e8 + the id of the way which is 32441915) if you, for example, are interested in the particular area in Cape Town;</li>
<li>I should have used "rel(bw:"outline")[type=building];" but as Maxerickson pointed out, the building school in Cape Town is a member of a multipolygon relation;</li>
<li>"way(r.relation:!"outline")" in your first query seems to be invalid as you can't use the unary operator'!' in front of a role;</li>
<li>"way["building"!="outline"](area)" in your second query is wrong ("outline" is a role and not the value of a tag).</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Feb '21, 15:01</strong></p>
<img src="https://secure.gravatar.com/avatar/9c8957ccf79025bf749665ebec2bdfa2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MarcoR&#39;s gravatar image" />
<p><span>MarcoR</span><br />
<span class="score" title="687 reputation points">687</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MarcoR has 5 accepted answers">23%</span> </br></p>
</div>
</div>
<div id="comments-container-78836" class="comments-container">
<span id="78908"></span>
<div id="comment-78908" class="comment">
<div id="post-78908-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/4426/insertuser"></a><a href="https://help.openstreetmap.org/users/4426/insertuser">@InsertUser</a> and <a href="https://help.openstreetmap.org/users/10973/maxerickson"></a><a href="https://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a> I am going to accept <a href="https://help.openstreetmap.org/users/6765/marcor"></a><a href="https://help.openstreetmap.org/users/6765/marcor">@MarcoR</a> 's answer as it does the necessary.</p>
<p>The result is <a href="https://github.com/AdrianKriger/osm_LoD1_3Dbuildings">here</a>. The data needs to be cleaned but its a strong foundation.</p>
<p>It would not have been possible without you. Thank you.</p>
</div>
<div id="comment-78908-info" class="comment-info">
<span class="comment-age">(17 Feb '21, 19:56)</span> <span class="comment-user userinfo">arkriger</span>
</div>
</div>
</div>
<div id="comment-tools-78836" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78836-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78807"></span>

<div id="answer-container-78807" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78807-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The item with role 'outline' is a multipolygon relation.</p>
<p>A different way to fetch the parts is to search on the <code>building:part</code> tag:</p>
<pre><code>[out:json][timeout:25];
area[name=&#39;Chapel Street Primary School&#39;];
way[&quot;building:part&quot;](area);
(._;&gt;;);
out;</code></pre>
<p>That may not work as well when searching a larger area though. My understanding is that objects should not usually have both <code>building:part</code> and <code>building</code> tags; if most of the data follows that it should work okay.</p>
<p>(the <code>building</code> relation is superfluous using that tagging style, there's no overlapping buildings to deal with and sometimes <code>building:part</code>s are available)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '21, 22:32</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-78807" class="comments-container">
<span id="78809"></span>
<div id="comment-78809" class="comment">
<div id="post-78809-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><code>outline</code> is not a valid role in <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon">multipolygons</a> (should be <code>outer</code>) , but is in relations of <a href="https://wiki.openstreetmap.org/wiki/Relation:building"><code>type=building</code></a>.</p>
</div>
<div id="comment-78809-info" class="comment-info">
<span class="comment-age">(12 Feb '21, 02:51)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="78812"></span>
<div id="comment-78812" class="comment">
<div id="post-78812-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. How would I now add the other <em>normal</em> buildings excluding the outline around a number of building:part (in the same query)?</p>
</div>
<div id="comment-78812-info" class="comment-info">
<span class="comment-age">(12 Feb '21, 10:37)</span> <span class="comment-user userinfo">arkriger</span>
</div>
</div>
<span id="78824"></span>
<div id="comment-78824" class="comment">
<div id="post-78824-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/4426/insertuser">@InsertUser</a>, the multipolygon is part of the building relation, with role 'outline'. I guess my other statement is not entirely clear.</p>
<p>I'm not sure how to reliably exclude the parent buildings; it may work well enough to construct a set by recursing up from the <code>building:parts</code>.</p>
<p>If there are no relations, then something like <code>way(around.parts:0)[building]</code> should detect overlapping buildings (where .parts is the building parts).</p>
</div>
<div id="comment-78824-info" class="comment-info">
<span class="comment-age">(12 Feb '21, 16:18)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="78825"></span>
<div id="comment-78825" class="comment">
<div id="post-78825-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a> I think I misread your opening sentence.</p>
</div>
<div id="comment-78825-info" class="comment-info">
<span class="comment-age">(12 Feb '21, 18:41)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-78807" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78807-form-container" class="comment-form-container">
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

