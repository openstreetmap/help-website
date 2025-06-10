+++
type = "question"
title = "Overpass Turbo: How to EXCLUDE tags that contain a string"
description = '''Hi, So you can go : to only include tags that have a certain string: name:foo (only places with foo anywhere in the name will show up), but I&#x27;m wondering if you can do the opposite, I want to EXCLUDE tags if they contain a certain word (I want every tag that does NOT contain the word foo in the exam...'''
date = "2021-05-12T22:53:00Z"
lastmod = "2021-05-14T16:30:00Z"
weight = 80141
keywords = [ "overpass", "contains", "overpass-turbo" ]
aliases = [ "/questions/80141" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass Turbo: How to EXCLUDE tags that contain a string](/questions/80141/overpass-turbo-how-to-exclude-tags-that-contain-a-string)

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
<span id="post-80141-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80141-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-80141-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>So you can go <strong>:</strong> to only include tags that have a certain string: name:foo (only places with foo anywhere in the name will show up), but I'm wondering if you can do the opposite, I want to EXCLUDE tags if they contain a certain word (I want every tag that does NOT contain the word foo in the example above).</p>
<p>I'm sure there must be a way, there's <strong>=</strong> and <strong>!=</strong>, so I'm sure they'll be some equivalent for contains, but it certainly isn't <strong><em>!:</em></strong> and I cannot find it in documentation.</p>
<p>Thanks in advance for your help, Steven.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-contains" rel="tag" title="see questions tagged &#39;contains&#39;">contains</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 May '21, 22:53</strong></p>
<img src="https://secure.gravatar.com/avatar/267550caa57a75fd02212654848033f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AutisticRabbit&#39;s gravatar image" />
<p><span>AutisticRabbit</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AutisticRabbit has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80141" class="comments-container">
<span id="80147"></span>
<div id="comment-80147" class="comment">
<div id="post-80147-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you provide an example illustrating what you want?</p>
</div>
<div id="comment-80147-info" class="comment-info">
<span class="comment-age">(13 May '21, 00:45)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="80149"></span>
<div id="comment-80149" class="comment">
<div id="post-80149-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm intrigued/confused by your first sentence. Do you have a working example to clarify what you mean?</p>
</div>
<div id="comment-80149-info" class="comment-info">
<span class="comment-age">(13 May '21, 02:39)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="80154"></span>
<div id="comment-80154" class="comment">
<div id="post-80154-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes sorry, so I am wanting to see all the churches of a specific denomination, but the denomination field isn't always filled in, so I will need to do some manual filtering. I thought a way to narrow down the list though would be to exclude results that mention a denomination in it's name, so for example if it was Trinity Evangelist Church, I want to exclude all names that contain the word Evangelist.</p>
<p><a href="https://help.openstreetmap.org/users/1532/davef"></a><a href="https://help.openstreetmap.org/users/1532/davef">@DaveF</a> Sorry what I was meaning by the first sentence is that I can do the opposite, I know how to ONLY find churches that have the word Evangelist in the name, but I don't know how to EXCLUDE churches that have the word Evangelist from the results.</p>
<p>Sorry for the confusion.</p>
</div>
<div id="comment-80154-info" class="comment-info">
<span class="comment-age">(13 May '21, 09:29)</span> <span class="comment-user userinfo">AutisticRabbit</span>
</div>
</div>
<span id="80161"></span>
<div id="comment-80161" class="comment">
<div id="post-80161-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Try with the operator "!~" which searches for values <em>not</em> matching a regular expression (<a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Value_matches_regular_expression_.28.7E.2C_.21.7E.29);">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Value_matches_regular_expression_.28.7E.2C_.21.7E.29);</a> please notice that not having the tag is considered a non match, thus it's shown in the result. If you want to avoid that, just add the filter ["name"]; Example: node["amenity"="place_of_worship"]["name"]["name"!~"Evangelist"](area.searchArea);</p>
</div>
<div id="comment-80161-info" class="comment-info">
<span class="comment-age">(13 May '21, 13:02)</span> <span class="comment-user userinfo">MarcoR</span>
</div>
</div>
<span id="80162"></span>
<div id="comment-80162" class="comment">
<div id="post-80162-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/6765/marcor">@MarcoR</a> Yes that worked! Thank you. If you post that as an answer, I will mark it as correct.</p>
</div>
<div id="comment-80162-info" class="comment-info">
<span class="comment-age">(13 May '21, 13:27)</span> <span class="comment-user userinfo">AutisticRabbit</span>
</div>
</div>
</div>
<div id="comment-tools-80141" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80141-form-container" class="comment-form-container">
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

<span id="80170"></span>

<div id="answer-container-80170" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80170-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-80170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AutisticRabbit has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>I know how to ONLY find churches that have the word Evangelist in the name, but I don't know how to EXCLUDE churches that have the word Evangelist from the results.</p>
</blockquote>
<p>Try with the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Value_matches_regular_expression_.28.7E.2C_.21.7E.29">operator "!~"</a> which searches for values not matching a regular expression.</p>
<p>Please note that not having the tag is considered a non match, thus it's shown in the result. If you want to avoid that, just add the filter ["name"].</p>
<p>Example:</p>
<pre><code>[out:json][timeout:25];
&#10;  nwr[&quot;amenity&quot;=&quot;place_of_worship&quot;][&quot;name&quot;][&quot;name&quot;!~&quot;Evangelist&quot;]({{bbox}});
&#10;out body;
&gt;;
out skel qt;</code></pre>
<p>Another way to obtain the same result is to use the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Difference">difference</a>:</p>
<pre><code>[out:json][timeout:25];
&#10;(
  nwr[&quot;amenity&quot;=&quot;place_of_worship&quot;][&quot;name&quot;]({{bbox}});
-
  nwr[&quot;amenity&quot;=&quot;place_of_worship&quot;][&quot;name&quot;~&quot;Evangelist&quot;]({{bbox}});
  );
out body;
&gt;;
out skel qt;</code></pre>
<p>The former should run faster but I think it depends on the area you are running it in.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 May '21, 18:47</strong></p>
<img src="https://secure.gravatar.com/avatar/9c8957ccf79025bf749665ebec2bdfa2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MarcoR&#39;s gravatar image" />
<p><span>MarcoR</span><br />
<span class="score" title="687 reputation points">687</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MarcoR has 5 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-80170" class="comments-container">
&#10;</div>
<div id="comment-tools-80170" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80170-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="80185"></span>

<div id="answer-container-80185" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80185-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80185-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80185-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Although MarcoR's former example is the preferable solution the 'difference' example, when it's the only option, can be improved slightly by passing the first call to a variable. In this example I display all edits for the last day except my own. (You'll need to add your own username)</p>
<pre><code>   (
    nwr(newer:&#39;{{date:24Hour}}&#39;)({{bbox}})-&gt;.Data;
    -
    nwr.Data(user:Joe_B);
   );
   out meta geom({{bbox}});</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '21, 16:30</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-80185" class="comments-container">
&#10;</div>
<div id="comment-tools-80185" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80185-form-container" class="comment-form-container">
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

