+++
type = "question"
title = "Cities from country via API"
description = '''Hi OSM-community! I am new to the subject, so I ask for a hint. I&#x27;ve found this awesome script: https://gist.github.com/4gus71n/26589a508d8deca333bb05928fd4beb0 which I try to modify. Line I am working on is: data = api.get(&#x27;area(&#x27;+str(id)+&#x27;)-&amp;gt;.a;(way(area.a)[&quot;name&quot;][&quot;highway&quot;][&quot;highway&quot; !~ &quot;path...'''
date = "2021-06-16T13:26:00Z"
lastmod = "2021-06-16T13:26:00Z"
weight = 80597
keywords = [ "overpassapi", "cities", "overpass-turbo" ]
aliases = [ "/questions/80597" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Cities from country via API](/questions/80597/cities-from-country-via-api)

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
<span id="post-80597-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80597-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80597-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi OSM-community! I am new to the subject, so I ask for a hint. I've found this awesome script: <a href="https://gist.github.com/4gus71n/26589a508d8deca333bb05928fd4beb0">https://gist.github.com/4gus71n/26589a508d8deca333bb05928fd4beb0</a> which I try to modify. Line I am working on is:</p>
<pre><code>data = api.get(&#39;area(&#39;+str(id)+&#39;)-&gt;.a;(way(area.a)[&quot;name&quot;][&quot;highway&quot;][&quot;highway&quot; !~ &quot;path&quot;]..blahblah..[&quot;highway&quot; !~ &quot;cycleway&quot;][&quot;foot&quot; !~ &quot;no&quot;][&quot;access&quot; !~ &quot;private&quot;][&quot;access&quot; !~ &quot;no&quot;];node(w)(area.a););out;&#39;)</code></pre>
<p>I try to make it get cities when given id of country. What I have for now is:</p>
<pre><code>data = api.get(&#39;area(&#39;+str(id)+&#39;)-&gt;.a;(node(area.a)[&quot;name&quot;][&quot;place&quot;=&quot;city&quot;];node(w)(area.a););out;&#39;)</code></pre>
<p>As you probably figured out - it does not work. I've tried many things and I'm unable to make it work. Could I ask for any hints? I also have tried to go with OverpassTurbo, but any query I fed was giving empty results.</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-cities" rel="tag" title="see questions tagged &#39;cities&#39;">cities</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jun '21, 13:26</strong></p>
<img src="https://secure.gravatar.com/avatar/d1d8c7f084a62c78fb4b054c47e718ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="siemaeniownik&#39;s gravatar image" />
<p><span>siemaeniownik</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="siemaeniownik has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jun '21, 13:27</strong> </span></p>
</div>
</div>
<div id="comments-container-80597" class="comments-container">
&#10;</div>
<div id="comment-tools-80597" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80597-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

