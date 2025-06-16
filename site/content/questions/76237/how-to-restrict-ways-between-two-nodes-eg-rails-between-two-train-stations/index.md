+++
type = "question"
title = "How to restrict ways between two nodes? (e.g. rails between two train stations)"
description = '''Hi, I want to restrict my search on Overpass Turbo to ways between 2 train stations. I have the UIC reference of the two stations, now I am only interested about the rails that connect the two stations. So I first look for the relations between the two stations, but that already gives me all relatio...'''
date = "2020-08-20T11:28:00Z"
lastmod = "2020-08-20T16:48:00Z"
weight = 76237
keywords = [ "ways", "overpass", "nodes", "waysbetweennodes", "overpass-turbo" ]
aliases = [ "/questions/76237" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to restrict ways between two nodes? (e.g. rails between two train stations)](/questions/76237/how-to-restrict-ways-between-two-nodes-eg-rails-between-two-train-stations)

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
<span id="post-76237-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76237-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76237-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,<br />
I want to restrict my search on Overpass Turbo to ways between 2 train stations. I have the UIC reference of the two stations, now I am only interested about the rails that connect the two stations.<br />
So I first look for the relations between the two stations, but that already gives me all relations of both stations. So I first like to restrict to only the relations going through both of these 2 train stations.<br />
Next I want only the ways along these relations between the two train stations.</p>
<p>Here is my code so far:</p>
<pre><code>[out:json][timeout:25];      
{{geocodeArea:Zurich}}-&gt;.searchArea;      
(        
  node[uicref=8503011][&quot;railway&quot;=&quot;station&quot;];    
  node[uicref=8503000][&quot;railway&quot;=&quot;station&quot;];    
  rel(bn);       
  way(r)(area.searchArea);   
);     
out body;    
&gt;;         
out skel qt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-waysbetweennodes" rel="tag" title="see questions tagged &#39;waysbetweennodes&#39;">waysbetweennodes</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Aug '20, 11:28</strong></p>
<img src="https://secure.gravatar.com/avatar/b6289de9e92470c9c0992be8b7ccdd18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roger&#39;s gravatar image" />
<p><span>Roger</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roger has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Aug '20, 16:57</strong> </span></p>
</div>
</div>
<div id="comments-container-76237" class="comments-container">
<span id="76238"></span>
<div id="comment-76238" class="comment">
<div id="post-76238-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please double check your code. It's returning empty.</p>
</div>
<div id="comment-76238-info" class="comment-info">
<span class="comment-age">(20 Aug '20, 11:43)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-76237" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76237-form-container" class="comment-form-container">
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

<span id="76239"></span>

<div id="answer-container-76239" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76239-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76239-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76239-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try this:</p>
<pre><code>[out:json][timeout:25];   
{{geocodeArea:Zurich}}-&gt;.searchArea;    
(    
  node[uic_ref=8503011][&quot;railway&quot;=&quot;station&quot;];  
  node[uic_ref=8503000][&quot;railway&quot;=&quot;station&quot;];  
  rel(bn)(area.searchArea);  
  way(r)(area.searchArea);  
);      
out body;    
&gt;;      
out skel qt;</code></pre>
<p>PS: I am interested only in the ways from Bhf. Wiedikon to HB Zürich, respectively the ways from the two nodes referenced by uic_ref above:</p>
<p><img src="/upfiles/Screen_Shot_2020-08-20_at_5.44.57_PM.png" alt="Bhf. Wiedikon to HB Zürich" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Aug '20, 16:48</strong></p>
<img src="https://secure.gravatar.com/avatar/b6289de9e92470c9c0992be8b7ccdd18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roger&#39;s gravatar image" />
<p><span>Roger</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roger has no accepted answers">0%</span> </br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Aug '20, 16:57</strong> </span></p>
</div>
</div>
<div id="comments-container-76239" class="comments-container">
&#10;</div>
<div id="comment-tools-76239" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76239-form-container" class="comment-form-container">
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

