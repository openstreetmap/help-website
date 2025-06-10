+++
type = "question"
title = "query 2 tags with OR statement"
description = '''This is a basic question, but it got me confused and I really can&#x27;T find anything. I&#x27;m a beginner with OSM, though got a map running with queries etc, all working fine. The thing is this: When working on a map which shows locations, I wanted to -for example- show vegan restaurants. Now there are a l...'''
date = "2019-01-06T14:19:00Z"
lastmod = "2019-01-08T22:04:00Z"
weight = 67463
keywords = [ "operator", "selection", "overpass-ql", "tags" ]
aliases = [ "/questions/67463" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [query 2 tags with OR statement](/questions/67463/query-2-tags-with-or-statement)

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
<span id="post-67463-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67463-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67463-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This is a basic question, but it got me confused and I really can'T find anything. I'm a beginner with OSM, though got a map running with queries etc, all working fine. The thing is this:</p>
<p>When working on a map which shows locations, I wanted to -for example- show vegan restaurants. Now there are a lot of different version tagged:</p>
<p>(EDIT: the option "diet:vegan" (yes, no, only) has the most places located, instead of the "diet"="vegan" used in my example)</p>
<p><code>place A - cuisine: vegan place B - diet:vegan: yes place C - diet:vegan place D - cuisine: vegetarian,_vegan,_veggie_burger</code></p>
<ul>
<li>If I use the basic query "cuisine=vegan" then result is only A.</li>
<li>when "diet=vegan" result is only C.</li>
<li>when going with a 'wildcard' ['cuisine'~'vegan',i] the result is only.. you guessed it.. A and D.</li>
</ul>
<p>Now my main question is: Is there a simple OR operator to use? These didn't work:</p>
<pre><code>[&#39;cuisine&#39;~&#39;vegan&#39;,i] | [&#39;diet&#39;~&#39;vegan&#39;,i]
[&#39;cuisine&#39;~&#39;vegan&#39;,i | &#39;diet&#39;~&#39;vegan&#39;,i]</code></pre>
<p>Then a not so important question/opinion left, but basically just to get more of in idea about the whole thing since I'll be needing it more with this project:</p>
<ul>
<li>What is the logic behind needing extra coding to find a tag that would be great to find with just one tag 'vegan' (result true or false) or something similar?</li>
</ul>
<p>I've read the documents on language and tagging, key etc, though can't understand the reason behind it. Of course there are thousands of possibilities to tag and it's been doing pretty great so far considering the size of the community working on it, though wouldn't it be an improvement keeping things like this a bit more basic and avoiding -for this example- the tags 'diet', 'cuisine' and just leave the options 'vegan' as a tag itself (true/false), maybe with option to go 'vegan:only'?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-operator" rel="tag" title="see questions tagged &#39;operator&#39;">operator</span> <span class="post-tag tag-link-selection" rel="tag" title="see questions tagged &#39;selection&#39;">selection</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jan '19, 14:19</strong></p>
<img src="https://secure.gravatar.com/avatar/89858e1d0e500ae658bf8cf7fc4964c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tijmenheid&#39;s gravatar image" />
<p><span>tijmenheid</span><br />
<span class="score" title="41 reputation points">41</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tijmenheid has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jan '19, 18:54</strong> </span></p>
</div>
</div>
<div id="comments-container-67463" class="comments-container">
<span id="67483"></span>
<div id="comment-67483" class="comment">
<div id="post-67483-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The reason you need "extra" queries is that there is no enforced or standardized tagging in OSM. Each mapper can choose to create his or her own version of the vegan tag, as you've just learned the hard way.</p>
<p>To make matters worse, many tags have spelling variations that are either intentional or accidental. These need to be accounted for too if you want complete results.</p>
</div>
<div id="comment-67483-info" class="comment-info">
<span class="comment-age">(07 Jan '19, 10:55)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="67488"></span>
<div id="comment-67488" class="comment">
<div id="post-67488-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks AlaskaDave, though i haven't seen the OSM editor but I was convinced there should be a pre-made list of tags to add on a click. Like "amenity is restaurant? well then here are all the standard tags: <em>listoftags</em>. Click to add. (max. 5)" Or something like that.</p>
<p>It might be an idea to filter out the non-registered tags (spelling variations etc) and add them to an 'extra' tag or something? f.e. [vegan:true, extra:vegan_pizza,vegetarian_pasta,etc]. Is there a good place to just dump ideas-that-might-work without having to discuss them?</p>
</div>
<div id="comment-67488-info" class="comment-info">
<span class="comment-age">(07 Jan '19, 16:29)</span> <span class="comment-user userinfo">tijmenheid</span>
</div>
</div>
<span id="67503"></span>
<div id="comment-67503" class="comment">
<div id="post-67503-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Currently there are <a href="https://taginfo.openstreetmap.org/reports/database_statistics">72 481 different keys with 99 519 867 different values</a>. One does not simply <del>walk into mordor</del> clean this up. Also see <a href="https://wiki.openstreetmap.org/wiki/Any_tags_you_like">any tags you like</a> for reasons why any mapper is allowed to create new tags.</p>
</div>
<div id="comment-67503-info" class="comment-info">
<span class="comment-age">(08 Jan '19, 08:00)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="67504"></span>
<div id="comment-67504" class="comment">
<div id="post-67504-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah I've seen that page, and haven'T walked into Mordor, since I'm not sure if they have good coffee. Referring to the tags, it was more to get back to the only applying principle of "Keep It Simple, Silly." So not the tag itself, but how to find it with 1 simple query, like it's supposed to.</p>
<p>In the 4 examples (mentioned in my question) using the proposed '=' operator, I would have to do a minimum of 4 queries to find 1 tag, and not many people are aware of that, which means they would miss out 30-60% of all vegan places on a map. I'm sure this is not the intention of 'Tags' and could be avoided by restricting the use of 'well-known' tags in certain keys and filtering out the ones with basic grammar-errors or just replace them to the right key.</p>
</div>
<div id="comment-67504-info" class="comment-info">
<span class="comment-age">(08 Jan '19, 10:38)</span> <span class="comment-user userinfo">tijmenheid</span>
</div>
</div>
<span id="67510"></span>
<div id="comment-67510" class="comment">
<div id="post-67510-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You can discuss all of this on the tagging list but there really won't be any resolution forthcoming. OSM tags are chaotic because it allows anyone the freedom to create any tag they like. On the one hand, this is wonderful and liberating but if you are forced to deal with it programmatically you have an uphill battle on your hands. OSM also strongly discourages any sort of mass-editing so in many cases, even that of a mis-spelled tag, errors can persist ad infinitum.</p>
<p>Welcome to the world of OSM.</p>
<p>You can signup for the tagging list here: <a href="https://lists.openstreetmap.org/listinfo/tagging">https://lists.openstreetmap.org/listinfo/tagging</a></p>
<p>Dave</p>
</div>
<div id="comment-67510-info" class="comment-info">
<span class="comment-age">(08 Jan '19, 14:37)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="67519"></span>
<div id="comment-67519" class="comment not_top_scorer">
<div id="post-67519-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok will give it a try, you never know, thanks for the info!</p>
</div>
<div id="comment-67519-info" class="comment-info">
<span class="comment-age">(08 Jan '19, 22:04)</span> <span class="comment-user userinfo">tijmenheid</span>
</div>
</div>
</div>
<div id="comment-tools-67463" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-67463-form-container" class="comment-form-container">
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

<span id="67467"></span>

<div id="answer-container-67467" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67467-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-67467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tijmenheid has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have to use the union "( )" operator in Overpass. The following query is constructed via the "Wizard" of OverpassTurbo. I just typed in "diet~vegan OR cuisine~vegan" and it gave me the query: <a href="http://overpass-turbo.eu/s/F1B">http://overpass-turbo.eu/s/F1B</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jan '19, 04:15</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-67467" class="comments-container">
<span id="67468"></span>
<div id="comment-67468" class="comment">
<div id="post-67468-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In case this website goes (temporarily) down, the resulting query is:</p>
<pre><code>[out:json][timeout:25];
// gather results
(
  // query part for: “diet~vegan”
  node[&quot;diet&quot;~&quot;vegan&quot;]({{bbox}});
  way[&quot;diet&quot;~&quot;vegan&quot;]({{bbox}});
  relation[&quot;diet&quot;~&quot;vegan&quot;]({{bbox}});
  // query part for: “cuisine~vegan”
  node[&quot;cuisine&quot;~&quot;vegan&quot;]({{bbox}});
  way[&quot;cuisine&quot;~&quot;vegan&quot;]({{bbox}});
  relation[&quot;cuisine&quot;~&quot;vegan&quot;]({{bbox}});
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
</div>
<div id="comment-67468-info" class="comment-info">
<span class="comment-age">(07 Jan '19, 07:39)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="67487"></span>
<div id="comment-67487" class="comment">
<div id="post-67487-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks mate! I didn'T knew about the 'wizard' menu in overpass-turbo, dôh! Learned it now.</p>
<p>Minimizing the code with the semi-new 'nwr[]', it would be: ( nwr<a href="%7B%7Bbbox%7D%7D">"diet"~"vegan"</a>;<br />
nwr<a href="%7B%7Bbbox%7D%7D">"cuisine"~"vegan"</a>; );</p>
<p>Will try it out!</p>
</div>
<div id="comment-67487-info" class="comment-info">
<span class="comment-age">(07 Jan '19, 16:12)</span> <span class="comment-user userinfo">tijmenheid</span>
</div>
</div>
</div>
<div id="comment-tools-67467" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67467-form-container" class="comment-form-container">
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

