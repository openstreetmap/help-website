+++
type = "question"
title = "How get all ways without ND tags"
description = '''Hello, I have this query, area[&quot;name&quot;=&quot;Greater London&quot;]; way(area)[&quot;amenity&quot;=&quot;restaurant&quot;]-&amp;gt;.all; ( .all; - ._; ); (._;); out geom;  which return me this result &amp;lt;way id=&quot;4270351&quot;&amp;gt;  &amp;lt;bounds minlat=&quot;51.6322589&quot; minlon=&quot;-0.0381454&quot; maxlat=&quot;51.6327917&quot; maxlon=&quot;-0.0376948&quot;/&amp;gt;  &amp;lt;nd ref=&quot;2...'''
date = "2018-01-26T14:29:00Z"
lastmod = "2018-01-28T18:10:00Z"
weight = 61819
keywords = [ "ways", "overpass", "overpass-turbo", "overpass-ql", "way" ]
aliases = [ "/questions/61819" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How get all ways without ND tags](/questions/61819/how-get-all-ways-without-nd-tags)

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
<span id="post-61819-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61819-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61819-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<pre><code>I have this query,
area[&quot;name&quot;=&quot;Greater London&quot;];
way(area)[&quot;amenity&quot;=&quot;restaurant&quot;]-&gt;.all;
( .all; - ._; );
(._;);
out geom;</code></pre>
<p>which return me this result</p>
<pre><code>&lt;way id=&quot;4270351&quot;&gt;
    &lt;bounds minlat=&quot;51.6322589&quot; minlon=&quot;-0.0381454&quot; maxlat=&quot;51.6327917&quot; maxlon=&quot;-0.0376948&quot;/&gt;
    &lt;nd ref=&quot;25637026&quot; lat=&quot;51.6327251&quot; lon=&quot;-0.0379737&quot;/&gt;
    &lt;nd ref=&quot;25637027&quot; lat=&quot;51.6327917&quot; lon=&quot;-0.0377806&quot;/&gt;
    &lt;nd ref=&quot;25637029&quot; lat=&quot;51.6326585&quot; lon=&quot;-0.0376948&quot;/&gt;
    &lt;nd ref=&quot;25637030&quot; lat=&quot;51.6323298&quot; lon=&quot;-0.0378665&quot;/&gt;
    &lt;nd ref=&quot;25637032&quot; lat=&quot;51.6322589&quot; lon=&quot;-0.0380668&quot;/&gt;
    &lt;nd ref=&quot;25637034&quot; lat=&quot;51.6324054&quot; lon=&quot;-0.0381454&quot;/&gt;
    &lt;nd ref=&quot;25637026&quot; lat=&quot;51.6327251&quot; lon=&quot;-0.0379737&quot;/&gt;
    &lt;tag k=&quot;amenity&quot; v=&quot;restaurant&quot;/&gt;
    &lt;tag k=&quot;building&quot; v=&quot;block&quot;/&gt;
    &lt;tag k=&quot;created_by&quot; v=&quot;JOSM&quot;/&gt;
  &lt;/way&gt;</code></pre>
<p>Is there a way get same but without ND tags? like this:</p>
<pre><code> &lt;way id=&quot;4270351&quot;&gt;
    &lt;bounds minlat=&quot;51.6322589&quot; minlon=&quot;-0.0381454&quot; maxlat=&quot;51.6327917&quot; maxlon=&quot;-0.0376948&quot;/&gt;
    &lt;tag k=&quot;amenity&quot; v=&quot;restaurant&quot;/&gt;
    &lt;tag k=&quot;building&quot; v=&quot;block&quot;/&gt;
    &lt;tag k=&quot;created_by&quot; v=&quot;JOSM&quot;/&gt;
  &lt;/way&gt;</code></pre>
<p>I will get needed lat lon from &lt;bounds&gt;, and in this case i don't want to get ND's because this tags make returned data <strong>heavy</strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jan '18, 14:29</strong></p>
<img src="https://secure.gravatar.com/avatar/237f0528f9712d0a3aa8736e5aa4a32c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="davittorosyan&#39;s gravatar image" />
<p><span>davittorosyan</span><br />
<span class="score" title="51 reputation points">51</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="davittorosyan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61819" class="comments-container">
&#10;</div>
<div id="comment-tools-61819" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61819-form-container" class="comment-form-container">
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

<span id="61821"></span>

<div id="answer-container-61821" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61821-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61821-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-61821-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>the ND-tags are the nodes. If you just want the center of the way, you could use "out center" instead of "out geom".</p>
<p>I'm not sure whether you can get the bounding box without the nodes. Both are part of the "out geom" statement</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jan '18, 14:34</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jan '18, 14:36</strong> </span></p>
</div>
</div>
<div id="comments-container-61821" class="comments-container">
<span id="61822"></span>
<div id="comment-61822" class="comment">
<div id="post-61822-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>and if you want all restaurants, you should also adapt your query to search for nodes and relations tagged with "amenity restaurant". So why not use <a href="http://overpass-turbo.eu/s/vpm">this query</a> instead ?</p>
<p>The query was almost completely constructed with the Wizard from "Overpass Turbo", I just replaced "geom" with "center" in the last line</p>
</div>
<div id="comment-61822-info" class="comment-info">
<span class="comment-age">(26 Jan '18, 14:39)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="61825"></span>
<div id="comment-61825" class="comment">
<div id="post-61825-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"out center" this is good solution tho have center point for each way, this will save my CPU to calculate center coordinate from &lt;bounds&gt; tag. But my problem little another now, i just don't want receive ND(node) tags, because instead of 5,000 lines XML file i receiving about 30,000(because this ND's very lot in each WAY tag) is there any solution to remove them from way tag but keep &lt; center &gt; tag?</p>
<p>without ND's but with all other tags(inlcuding &lt; center &gt; tag)</p>
</div>
<div id="comment-61825-info" class="comment-info">
<span class="comment-age">(26 Jan '18, 15:37)</span> <span class="comment-user userinfo">davittorosyan</span>
</div>
</div>
<span id="61848"></span>
<div id="comment-61848" class="comment">
<div id="post-61848-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>did you take the take to look at the data from the query I linked to ? There are no ND tags when you use out center</p>
</div>
<div id="comment-61848-info" class="comment-info">
<span class="comment-age">(27 Jan '18, 19:06)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="61849"></span>
<div id="comment-61849" class="comment">
<div id="post-61849-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes, thank you for example, but sorry, I cant use this csv:out format for getting data ... because my parsers working with XML, but main reason, i dont want use out:csv, because each way object can have different parameters, phone, fax, opening_hours etc... but in your example i should predefine fields</p>
<p>[out:csv( ::"id", ::lat, ::lon, name, cuisine, operator, "contact:website", "contact:phone"; true; "|" )];</p>
<p>is there another way to have my wanted format? Or its impossible? thank you</p>
</div>
<div id="comment-61849-info" class="comment-info">
<span class="comment-age">(27 Jan '18, 19:24)</span> <span class="comment-user userinfo">davittorosyan</span>
</div>
</div>
<span id="61850"></span>
<div id="comment-61850" class="comment">
<div id="post-61850-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The query I link to returns XML. (see "this query" two comments back)</p>
<p>And as for the output formats, please try the different output statements that are shown in the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Control_output_format_.28print.2C_out.29">documentation</a> if the format that you want is not between them, you can perhaps create a feature request.</p>
<p>And otherwise, the extra data can easily be ignored by any decent XML parser. I doubt that your computer cannot handle the extra information in a quick way. 5000 lines of XML is nothing for today's CPUs</p>
</div>
<div id="comment-61850-info" class="comment-info">
<span class="comment-age">(27 Jan '18, 19:36)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="61852"></span>
<div id="comment-61852" class="comment not_top_scorer">
<div id="post-61852-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for answer, i will check is this solution for me.</p>
</div>
<div id="comment-61852-info" class="comment-info">
<span class="comment-age">(27 Jan '18, 19:58)</span> <span class="comment-user userinfo">davittorosyan</span>
</div>
</div>
</div>
<div id="comment-tools-61821" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-61821-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61823"></span>

<div id="answer-container-61823" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61823-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61823-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61823-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know how to get rid of the node references (nd) as you ask for output, but I guess that what you want is a kind of csv-like output with the info of the ways for restaurants. In that case, you have the csv output mode.</p>
<p>For your example, you could try with:</p>
<pre><code>[out:csv(
::&quot;id&quot;, ::lat, ::lon, name, cuisine, operator, &quot;contact:website&quot;, &quot;contact:phone&quot;;
    true; &quot;|&quot;
  )];
area[&quot;name&quot;=&quot;Greater London&quot;];
way(area)[&quot;amenity&quot;=&quot;restaurant&quot;]-&gt;.all;
( .all; - ._; );
(._;);
out center;</code></pre>
<p>If you delete the</p>
<pre><code>; &quot;|&quot;</code></pre>
<p>you will get the fields separated by a tab. You can also substitute the | by another string that suits you better.</p>
<p>You have much more info on that csv mode <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#CSV_output_mode">here</a>, specially about the fields you can add...</p>
<p>I hope this suits you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jan '18, 14:58</strong></p>
<img src="https://secure.gravatar.com/avatar/d45c161edd4b471fd947a7ec574274ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edvac&#39;s gravatar image" />
<p><span>edvac</span><br />
<span class="score" title="665 reputation points">665</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edvac has 4 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jan '18, 15:07</strong> </span></p>
</div>
</div>
<div id="comments-container-61823" class="comments-container">
<span id="61856"></span>
<div id="comment-61856" class="comment">
<div id="post-61856-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>One of stackoverflow OSM developers find the solution, just need write "tags" in OUT:</p>
<p>out tags;</p>
</div>
<div id="comment-61856-info" class="comment-info">
<span class="comment-age">(28 Jan '18, 15:23)</span> <span class="comment-user userinfo">davittorosyan</span>
</div>
</div>
<span id="61859"></span>
<div id="comment-61859" class="comment">
<div id="post-61859-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah! Good! Didn't know that option :)</p>
</div>
<div id="comment-61859-info" class="comment-info">
<span class="comment-age">(28 Jan '18, 18:10)</span> <span class="comment-user userinfo">edvac</span>
</div>
</div>
</div>
<div id="comment-tools-61823" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61823-form-container" class="comment-form-container">
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

