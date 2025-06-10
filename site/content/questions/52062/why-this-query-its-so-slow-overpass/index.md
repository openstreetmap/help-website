+++
type = "question"
title = "Why this query it&#x27;s so slow (Overpass)?"
description = '''Hi, I want to get an intersection between two streets in my city using Overpass API. When I execute it, the response takes 2 minutes or more. Using overpass turbo: area[name=&quot;Montevideo&quot;]-&amp;gt;.boundaryarea; way(area.boundaryarea)[highway][name=&quot;Avenida Italia&quot;];node(w)-&amp;gt;.n1; way(area.boundaryarea...'''
date = "2016-09-15T18:55:00Z"
lastmod = "2016-09-15T20:59:00Z"
weight = 52062
keywords = [ "overpassapi", "intersection" ]
aliases = [ "/questions/52062" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why this query it's so slow (Overpass)?](/questions/52062/why-this-query-its-so-slow-overpass)

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
<span id="post-52062-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52062-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52062-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I want to get an intersection between two streets in my city using Overpass API. When I execute it, the response takes 2 minutes or more.</p>
<p>Using overpass turbo:</p>
<pre><code>area[name=&quot;Montevideo&quot;]-&gt;.boundaryarea;
way(area.boundaryarea)[highway][name=&quot;Avenida Italia&quot;];node(w)-&gt;.n1;
way(area.boundaryarea)[highway][name=&quot;Avenida Bolivia&quot;];node(w)-&gt;.n2;
node.n1.n2;
out meta;</code></pre>
<p>Using the browser:</p>
<pre><code>http://overpass-api.de/api/interpreter?data=area[name=&quot;Montevideo&quot;]-&gt;.boundaryarea;way(area.boundaryarea)[highway][name=&quot;Avenida Italia&quot;];node(w)-&gt;.n1;way(area.boundaryarea)[highway][name=&quot;Avenida Bolivia&quot;];node(w)-&gt;.n2;node.n1.n2;out;</code></pre>
<p>Mybe I made the wrong filter?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-intersection" rel="tag" title="see questions tagged &#39;intersection&#39;">intersection</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Sep '16, 18:55</strong></p>
<img src="https://secure.gravatar.com/avatar/824548f7e6ef9be42ae61003bf31639b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PabloGarin&#39;s gravatar image" />
<p><span>PabloGarin</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PabloGarin has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Sep '16, 09:25</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span></p>
</div>
</div>
<div id="comments-container-52062" class="comments-container">
<span id="52063"></span>
<div id="comment-52063" class="comment">
<div id="post-52063-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>general note: this help system keeps linking only a part of the URL, despite the "code" formatting.. just copy and paste it to try the URL.</p>
</div>
<div id="comment-52063-info" class="comment-info">
<span class="comment-age">(15 Sep '16, 20:59)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-52062" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52062-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

