+++
type = "question"
title = "Districts&#x27; names with state names as CSV with Overpass API"
description = '''I am looking district names of India with state names as CSV format. I tried to write an overpass query but it is not working. Please let me know what I am doing wrong. Is there any other simple query also. I am looking only from Overpass API not from any other data provider. [out:csv(::type,::id,ad...'''
date = "2023-10-25T08:32:00Z"
lastmod = "2023-10-26T18:26:00Z"
weight = 87936
keywords = [ "overpass" ]
aliases = [ "/questions/87936" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Districts' names with state names as CSV with Overpass API](/questions/87936/districts-names-with-state-names-as-csv-with-overpass-api)

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
<span id="post-87936-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87936-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87936-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am looking district names of India with state names as CSV format. I tried to write an overpass query but it is not working. Please let me know what I am doing wrong. Is there any other simple query also. I am looking only from Overpass API not from any other data provider.</p>
<pre><code>[out:csv(::type,::id,admin_level,name,&quot;name:en&quot;,&quot;country&quot;,&quot;admin_level_4_name&quot;)];
&#10;rel[&quot;name:en&quot;=&quot;India&quot;]-&gt;.rel;
map_to_area-&gt;.a;
&#10;(
    rel[admin_level=4](area.a)-&gt;.admin_level_4;
    rel[admin_level=5](area.a)-&gt;.admin_level_5;
    foreach.admin_level_5(
        out center -&gt;.ctr;
        .ctr is_in-&gt;.admin_level_4_relation;
        .admin_level_5 set admin_level_4_name = .admin_level_4_relation[&quot;name&quot;];
        out;
    );
);
&#10;out;</code></pre>
<p><strong>Update 1:</strong></p>
<p>I am adding here the overpass-turbo error:</p>
<pre><code>An error occurred during the execution of the overpass query! This is what overpass API returned:
&#10;Error: line 10: parse error: Invalid parameter for print: &quot;-&gt;&quot;
Error: line 10: parse error: Invalid parameter for print: &quot;.&quot;
Error: line 10: parse error: Invalid parameter for print: &quot;ctr&quot;
Error: line 12: parse error: &#39;;&#39; expected - &#39;set&#39; found.</code></pre>
<p>Link to overpass-turbo for <a href="https://overpass-turbo.eu/s/1CtV">this routine</a>.</p>
<p><strong>Update 2:</strong></p>
<p>As per DaveF suggestions here is the modified the query. Now not able to make out how to set admin_level 4 names to admin_level 5.</p>
<pre><code>[out:csv(::type,::id,admin_level,name,&quot;name:en&quot;,&quot;country&quot;,&quot;admin_level_4_name&quot;)];
rel[&quot;name:en&quot;=&quot;India&quot;];
map_to_area-&gt;.a;
(
    rel[admin_level=4](area.a)-&gt;.admin_level_4;
    rel[admin_level=5](area.a)-&gt;.admin_level_5;
    foreach.admin_level_5(
        out center;
        is_in-&gt;.admin_level_4_relation;
        // not able to make out how to set level 4 name to level 5 relation
        convert rel ::=::; 
        out;
    );
 );</code></pre>
<p>Overpass turbo <a href="https://overpass-turbo.eu/s/1CuS">link for above query</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '23, 08:32</strong></p>
<img src="https://secure.gravatar.com/avatar/39d75f04e1a21ba653b41ac75ec1b026?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gagan&#39;s gravatar image" />
<p><span>Gagan</span><br />
<span class="score" title="305 reputation points">305</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gagan has 2 accepted answers">14%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Oct '23, 17:59</strong> </span></p>
</div>
</div>
<div id="comments-container-87936" class="comments-container">
<span id="87944"></span>
<div id="comment-87944" class="comment">
<div id="post-87944-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It seems inconceivable you got to this stage by building the routine step by step. Start with the basics. Tip: you don't need to put every output into a named set. Try passing level 5 to the foreach</p>
</div>
<div id="comment-87944-info" class="comment-info">
<span class="comment-age">(25 Oct '23, 16:07)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="87948"></span>
<div id="comment-87948" class="comment">
<div id="post-87948-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/1532/davef">@Davef</a> I have added the overpass-turbo error also. I suppose I am looping through the admin_level_5 only or is this not the correct way to loop?</p>
</div>
<div id="comment-87948-info" class="comment-info">
<span class="comment-age">(26 Oct '23, 11:32)</span> <span class="comment-user userinfo">Gagan</span>
</div>
</div>
<span id="87949"></span>
<div id="comment-87949" class="comment">
<div id="post-87949-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you provide urls to an example of what your searching for? Both the district &amp; state.</p>
</div>
<div id="comment-87949-info" class="comment-info">
<span class="comment-age">(26 Oct '23, 14:48)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="87950"></span>
<div id="comment-87950" class="comment">
<div id="post-87950-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Here are URLs for <a href="https://en.wikipedia.org/wiki/States_and_union_territories_of_India">India's states</a> admin_level 4 and <a href="https://en.wikipedia.org/wiki/List_of_districts_in_India">districts</a> admin_level 5.</p>
</div>
<div id="comment-87950-info" class="comment-info">
<span class="comment-age">(26 Oct '23, 18:02)</span> <span class="comment-user userinfo">Gagan</span>
</div>
</div>
<span id="87951"></span>
<div id="comment-87951" class="comment">
<div id="post-87951-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think <a href="https://overpass-turbo.eu/s/1CuZ">this query</a> would help me. This is based on this <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#Adding_Georeference_details_to_village_nodes_(since_0.7.54)">example</a></p>
</div>
<div id="comment-87951-info" class="comment-info">
<span class="comment-age">(26 Oct '23, 18:26)</span> <span class="comment-user userinfo">Gagan</span>
</div>
</div>
</div>
<div id="comment-tools-87936" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87936-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

