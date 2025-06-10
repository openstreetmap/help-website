+++
type = "question"
title = "Find objects with duplicate tag"
description = '''I would like to find all relations that have duplicate wikidata tags. I saw finding dup nodes, but cannot figure out how to adaapt my query to it: [out:csv(admin_level,::id,wikidata,name,wikipedia,boundary,type,alt_name,designation)]; (  rel[&quot;admin_level&quot;][&quot;wikidata&quot;]; );'''
date = "2017-01-03T08:06:00Z"
lastmod = "2017-09-06T09:08:00Z"
weight = 53811
keywords = [ "overpass", "overpass-turbo" ]
aliases = [ "/questions/53811" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Find objects with duplicate tag](/questions/53811/find-objects-with-duplicate-tag)

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
<span id="post-53811-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53811-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53811-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to find all relations that have duplicate wikidata tags. I saw <a href="https://help.openstreetmap.org/questions/39745/show-duplicated-nodes-via-overpass">finding dup nodes</a>, but cannot figure out how to adaapt my query to it:</p>
<p><code>[out:csv(admin_level,::id,wikidata,name,wikipedia,boundary,type,alt_name,designation)]; ( rel["admin_level"]["wikidata"]; );</code></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jan '17, 08:06</strong></p>
<img src="https://secure.gravatar.com/avatar/d46d9a8875ccdaa0b3b39bf485df3ead?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nyuriks&#39;s gravatar image" />
<p><span>nyuriks</span><br />
<span class="score" title="71 reputation points">71</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nyuriks has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jan '17, 19:34</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/eca34689e074411e0daca0d994f532b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tyr_asd&#39;s gravatar image" />
<p><span>tyr_asd</span><br />
<span class="score" title="1196 reputation points"><span>1.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span></p>
</div>
</div>
<div id="comments-container-53811" class="comments-container">
&#10;</div>
<div id="comment-tools-53811" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53811-form-container" class="comment-form-container">
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

<span id="59408"></span>

<div id="answer-container-59408" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59408-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59408-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59408-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The new <a href="https://wiki.openstreetmap.org/wiki/Wikidata%2BOSM_SPARQL_query_service">OSM+Wikidata SPARQL service</a> can now do it with <a href="https://wiki.openstreetmap.org/wiki/SPARQL_examples#Find_when_more_than_one_relation_link_to_the_same_Wikidata_ID">this query</a>.</p>
<pre><code>SELECT ?osmid ?adminlvl ?wd ?wdLabel {
  # find relation with a wikidata tag
  ?osmid osmm:type &#39;r&#39; ;
         osmt:wikidata ?wd ;
         osmt:admin_level ?adminlvl .
&#10;  # add user&#39;s or english label to the found wikidata
  SERVICE wikibase:label { bd:serviceParam wikibase:language &quot;[AUTO_LANGUAGE],en&quot;. }
&#10;  # the ?wd variable must also be matching this subquery
  # it finds wd tags that appear more than once
  { SELECT ?wd { 
    ?osmid osmm:type &#39;r&#39; ;
           osmt:wikidata ?wd ;
           osmt:admin_level ?adminlvl .
    }
    GROUP BY ?wd
    HAVING (COUNT(*) &gt; 1)
  }
&#10;} LIMIT 10</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '17, 09:08</strong></p>
<img src="https://secure.gravatar.com/avatar/d46d9a8875ccdaa0b3b39bf485df3ead?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nyuriks&#39;s gravatar image" />
<p><span>nyuriks</span><br />
<span class="score" title="71 reputation points">71</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nyuriks has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-59408" class="comments-container">
&#10;</div>
<div id="comment-tools-59408" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59408-form-container" class="comment-form-container">
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

