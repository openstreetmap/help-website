+++
type = "question"
title = "Grouping multiple categories in Overpass Turbo"
description = '''Hello guys, I have UNION query area[&quot;name&quot;=&quot;London&quot;][&quot;admin_level&quot;=&quot;6&quot;]; node(area)[&quot;amenity&quot;=&quot;cafe&quot;]-&amp;gt;.cafe; node(area)[&quot;amenity&quot;=&quot;bar&quot;]-&amp;gt;.bar; ( .cafe; .bar; )-&amp;gt;.all; ( .all; - ._; ); (._;); out;  all is working good BUT is there a way to grouping the received Nodes(or ways) like this? &amp;l...'''
date = "2018-02-01T16:21:00Z"
lastmod = "2018-02-06T14:47:00Z"
weight = 61923
keywords = [ "overpassapi", "overpass", "overpass-turbo", "overpass-ql" ]
aliases = [ "/questions/61923" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [Grouping multiple categories in Overpass Turbo](/questions/61923/grouping-multiple-categories-in-overpass-turbo)

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
<span id="post-61923-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61923-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61923-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello guys,</p>
<p>I have UNION query</p>
<pre><code>area[&quot;name&quot;=&quot;London&quot;][&quot;admin_level&quot;=&quot;6&quot;];
node(area)[&quot;amenity&quot;=&quot;cafe&quot;]-&gt;.cafe;
node(area)[&quot;amenity&quot;=&quot;bar&quot;]-&gt;.bar;
(
.cafe;
.bar;
)-&gt;.all;
( .all; - ._; );
(._;);
out;</code></pre>
<p><strong>all is working good</strong></p>
<p>BUT is there a way to grouping the received Nodes(or ways) like this?</p>
<pre><code>&lt;cafe&gt;
  &lt;node id=&quot;20849687&quot; lat=&quot;51.4111705&quot; lon=&quot;-0.3339165&quot;&gt;
    &lt;tag k=&quot;amenity&quot; v=&quot;cafe&quot;/&gt;
    &lt;tag k=&quot;note&quot; v=&quot;is a trailer parked there, serving tea, sandwiches, ice-cream etc.&quot;/&gt;
    &lt;tag k=&quot;operator&quot; v=&quot;ECSI Limited&quot;/&gt;
  &lt;/node&gt;
  &lt;node id=&quot;25475389&quot; lat=&quot;51.5265807&quot; lon=&quot;-0.1292505&quot;&gt;
    &lt;tag k=&quot;amenity&quot; v=&quot;cafe&quot;/&gt;
    &lt;tag k=&quot;fixme&quot; v=&quot;not on FHRS&quot;/&gt;
    &lt;tag k=&quot;name&quot; v=&quot;Woburn Cafe&quot;/&gt;
  &lt;/node&gt;
  ...etc (all cafes)
&lt;/cafe&gt;
&lt;bar&gt;
  &lt;node id=&quot;21593237&quot; lat=&quot;51.5173465&quot; lon=&quot;-0.1189566&quot;&gt;
    &lt;tag k=&quot;amenity&quot; v=&quot;bar&quot;/&gt;
    &lt;tag k=&quot;cuisine&quot; v=&quot;polish&quot;/&gt;
    &lt;tag k=&quot;food&quot; v=&quot;yes&quot;/&gt;
    &lt;tag k=&quot;name&quot; v=&quot;Bar Polski&quot;/&gt;
    &lt;tag k=&quot;toilets&quot; v=&quot;yes&quot;/&gt;
    &lt;tag k=&quot;toilets:access&quot; v=&quot;customers&quot;/&gt;
  &lt;/node&gt;
  ...etc (all bars)
&lt;/bar&gt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Feb '18, 16:21</strong></p>
<img src="https://secure.gravatar.com/avatar/237f0528f9712d0a3aa8736e5aa4a32c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="davittorosyan&#39;s gravatar image" />
<p><span>davittorosyan</span><br />
<span class="score" title="51 reputation points">51</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="davittorosyan has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Feb '18, 19:38</strong> </span></p>
</div>
</div>
<div id="comments-container-61923" class="comments-container">
&#10;</div>
<div id="comment-tools-61923" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61923-form-container" class="comment-form-container">
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

5 Answers:

</div>

</div>

<span id="61925"></span>

<div id="answer-container-61925" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61925-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To group the results, get rid of the union and repeat the <code>out</code> statement (untested):</p>
<pre><code>area[&quot;name&quot;=&quot;London&quot;][&quot;admin_level&quot;=&quot;6&quot;]-&gt;.searchArea;
node(area.searchArea)[&quot;amenity&quot;=&quot;cafe&quot;];
out;
node(area.searchArea)[&quot;amenity&quot;=&quot;bar&quot;];
out;</code></pre>
<p>They won't be grouped under cafe and bar elements in the output but they will be separated by type.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Feb '18, 21:20</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Feb '18, 00:31</strong> </span></p>
</div>
</div>
<div id="comments-container-61925" class="comments-container">
<span id="61926"></span>
<div id="comment-61926" class="comment">
<div id="post-61926-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, but don't works, only show the "Cafe" results. is there a way for example add some separator between categories? For example -------, or +++++ ?</p>
</div>
<div id="comment-61926-info" class="comment-info">
<span class="comment-age">(02 Feb '18, 06:01)</span> <span class="comment-user userinfo">davittorosyan</span>
</div>
</div>
<span id="61947"></span>
<div id="comment-61947" class="comment">
<div id="post-61947-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, the <code>bar</code> query didn't have any areas to search in. I've amended the query to save the search area to a set.</p>
</div>
<div id="comment-61947-info" class="comment-info">
<span class="comment-age">(04 Feb '18, 00:30)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-61925" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61925-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61928"></span>

<div id="answer-container-61928" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61928-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61928-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61928-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sorry, but AFAIK, it is not possible as maxerickson already indicated. You try to introduce a tags that does not exist in the OSM model (bar &amp; cafe).</p>
<p>You have to be aware that Overpass is just a very thin layer above the raw OSM data. Although it's powerful, you are still expected to write some code to format the result in the model you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Feb '18, 10:25</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-61928" class="comments-container">
<span id="61935"></span>
<div id="comment-61935" class="comment">
<div id="post-61935-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>amenity=cafe and amenity=bar are widely used tags, so I'm not sure what you mean here.</p>
</div>
<div id="comment-61935-info" class="comment-info">
<span class="comment-age">(02 Feb '18, 16:28)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="61937"></span>
<div id="comment-61937" class="comment">
<div id="post-61937-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/8189/alester">@alester</a> I mean can we somehow separate the results with some custom separators?</p>
</div>
<div id="comment-61937-info" class="comment-info">
<span class="comment-age">(02 Feb '18, 16:49)</span> <span class="comment-user userinfo">davittorosyan</span>
</div>
</div>
<span id="61938"></span>
<div id="comment-61938" class="comment">
<div id="post-61938-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>They are widely used as value for v (see XML above), not as tag e. g. &lt;pub&gt;. The OP tries to create a whole new XML format. This is not possible server side and should be done locally</p>
</div>
<div id="comment-61938-info" class="comment-info">
<span class="comment-age">(02 Feb '18, 17:39)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-61928" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61928-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61949"></span>

<div id="answer-container-61949" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61949-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61949-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61949-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you guys for answers, but lets think from another angle of view</p>
<p>What if we will have one querie for pub and bars and between this 2 results insert additional line(for example "+++" this line)? Or this is also mran structure changing? My problem im 2 words - have 1 query but separate results in response.</p>
<p>Response I need, should be like this:</p>
<pre><code>Pubs
+++
Bars
+++
Restaurants
+++
Fast foods
+++
Ets...</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Feb '18, 15:04</strong></p>
<img src="https://secure.gravatar.com/avatar/237f0528f9712d0a3aa8736e5aa4a32c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="davittorosyan&#39;s gravatar image" />
<p><span>davittorosyan</span><br />
<span class="score" title="51 reputation points">51</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="davittorosyan has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Feb '18, 15:10</strong> </span></p>
</div>
</div>
<div id="comments-container-61949" class="comments-container">
<span id="61954"></span>
<div id="comment-61954" class="comment">
<div id="post-61954-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can use the <code>make</code> statement to insert elements between the <code>out</code> statements.</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#The_make_statement">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#The_make_statement</a></p>
</div>
<div id="comment-61954-info" class="comment-info">
<span class="comment-age">(05 Feb '18, 00:31)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="61960"></span>
<div id="comment-61960" class="comment">
<div id="post-61960-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a> wow...thanks a lot finally i can see something, which can help resolve my problem. Can you see my comment below please.</p>
</div>
<div id="comment-61960-info" class="comment-info">
<span class="comment-age">(05 Feb '18, 13:30)</span> <span class="comment-user userinfo">davittorosyan</span>
</div>
</div>
</div>
<div id="comment-tools-61949" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61949-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61961"></span>

<div id="answer-container-61961" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61961-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61961-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61961-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks <a href="https://help.openstreetmap.org/users/10973/maxerickson"></a><a href="https://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a></a> for solution, if you can please help me here also: I Have this part of code, and this is works good, my custom tag inserted with separate OUT in end of whole XML:</p>
<pre><code>area[&quot;name&quot;=&quot;London&quot;][&quot;admin_level&quot;=&quot;6&quot;];
node(area)[&quot;amenity&quot;=&quot;cafe&quot;]-&gt;.cafe;
node(area)[&quot;amenity&quot;=&quot;bar&quot;]-&gt;.bar;
&#10;
(
&#10;.cafe;
.bar;
&#10;)-&gt;.all;
&#10;
( .all; - ._; );
&#10;(._;);
&#10;
out;
&#10;make my_element_name                           
     ::id = 1234,                            
     &quot;tag1&quot; = &quot;this is the value of tag1&quot;,    
     &quot;tag2&quot; = 4711,                          
     &quot;tag3&quot; = date(&quot;2018-07-01&quot;);             
out;</code></pre>
<p><strong>is there solution to insert many custom tags after each category, for eaxmple?:</strong></p>
<pre><code>Cafes
&lt;my_element_name1&gt;
Bars
&lt;my_element_name2&gt;
etc...</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Feb '18, 14:06</strong></p>
<img src="https://secure.gravatar.com/avatar/237f0528f9712d0a3aa8736e5aa4a32c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="davittorosyan&#39;s gravatar image" />
<p><span>davittorosyan</span><br />
<span class="score" title="51 reputation points">51</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="davittorosyan has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Feb '18, 14:07</strong> </span></p>
</div>
</div>
<div id="comments-container-61961" class="comments-container">
<span id="61976"></span>
<div id="comment-61976" class="comment">
<div id="post-61976-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Simply place multiple make statements in the script.</p>
</div>
<div id="comment-61976-info" class="comment-info">
<span class="comment-age">(06 Feb '18, 00:36)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="61978"></span>
<div id="comment-61978" class="comment">
<div id="post-61978-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>sorry if my question will sounds simple...but i'm not expert on overpass queries.. but in my concept of query i wrote above in this comment, how can i place multiple "make"? this is union query and I cant imagine how i can insert between categories my "make"-s. can you please wrote example?</p>
</div>
<div id="comment-61978-info" class="comment-info">
<span class="comment-age">(06 Feb '18, 06:18)</span> <span class="comment-user userinfo">davittorosyan</span>
</div>
</div>
<span id="61979"></span>
<div id="comment-61979" class="comment">
<div id="post-61979-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>UPDATE. <a href="https://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a> I have some progress, please see comment below.</p>
</div>
<div id="comment-61979-info" class="comment-info">
<span class="comment-age">(06 Feb '18, 07:11)</span> <span class="comment-user userinfo">davittorosyan</span>
</div>
</div>
</div>
<div id="comment-tools-61961" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61961-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61980"></span>

<div id="answer-container-61980" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61980-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61980-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61980-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have some progress... current query</p>
<pre><code>area[&quot;name&quot;=&quot;London&quot;][&quot;admin_level&quot;=&quot;6&quot;];
node(area)[&quot;amenity&quot;=&quot;cafe&quot;]-&gt;.cafe;
node(area)[&quot;amenity&quot;=&quot;bar&quot;]-&gt;.bar;
&#10;make node                           
     ::id = 1,                            
     &quot;tag1&quot; = &quot;aaa&quot;,    
     &quot;tag2&quot; = 4711,                          
     &quot;tag3&quot; = date(&quot;2018-07-01&quot;)-&gt;.my_custom_node1;
&#10;make node                           
     ::id = 2,                            
     &quot;tag1&quot; = &quot;bbb&quot;,    
     &quot;tag2&quot; = 4711,                          
     &quot;tag3&quot; = date(&quot;2018-07-01&quot;)-&gt;.my_custom_node2;
&#10;(
&#10;  .cafe;
  .my_custom_node1;
  .bar;
  .my_custom_node2;
&#10;)-&gt;.all;
&#10;
( .all; - ._; );
&#10;(._;);
&#10;
out;</code></pre>
<p>ONLY one problem i have now - ORDERING. I Know, Overpass by default return ordered by id, but is there a way, get response with this ordering ?</p>
<pre><code>&lt;cafe&gt;(all cafes)
&lt;my_custom_node1&gt;
&lt;bar&gt;(all bars)
&lt;my_custom_node2&gt;</code></pre>
<p>because currently this 2 custom tags added in very bottom of the whole result.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Feb '18, 07:16</strong></p>
<img src="https://secure.gravatar.com/avatar/237f0528f9712d0a3aa8736e5aa4a32c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="davittorosyan&#39;s gravatar image" />
<p><span>davittorosyan</span><br />
<span class="score" title="51 reputation points">51</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="davittorosyan has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Feb '18, 07:16</strong> </span></p>
</div>
</div>
<div id="comments-container-61980" class="comments-container">
<span id="61984"></span>
<div id="comment-61984" class="comment">
<div id="post-61984-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You need to use multiple out statements, like in my earlier answer.</p>
<p>Note that <code>( .all; - ._; );</code> and <code>(._;);</code> aren't doing much in your script. The statement ending in <code>-&gt;.all</code> leaves the default set (<code>._</code>) empty and those statements say "Subtract an empty set from my results and store it in <code>._</code>" and "take the current default set and store it in the default set". Eliminating those two statements and using <code>.all out;</code> is a more direct way of doing the same thing.</p>
<p>Anyway, to get results all together with ordering determined by the server, use a union. To get results in an order that you determine, use multiple out statements.</p>
</div>
<div id="comment-61984-info" class="comment-info">
<span class="comment-age">(06 Feb '18, 12:51)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="61987"></span>
<div id="comment-61987" class="comment">
<div id="post-61987-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a> you are one of the best Overpass QL masters. Thanks a lot for finding solution for this problem. Works fine for me, Thanks again</p>
</div>
<div id="comment-61987-info" class="comment-info">
<span class="comment-age">(06 Feb '18, 14:47)</span> <span class="comment-user userinfo">davittorosyan</span>
</div>
</div>
</div>
<div id="comment-tools-61980" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61980-form-container" class="comment-form-container">
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

