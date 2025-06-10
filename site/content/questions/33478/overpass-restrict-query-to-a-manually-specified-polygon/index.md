+++
type = "question"
title = "Overpass: restrict query to a manually-specified polygon"
description = '''I have a simple Overpass XML query, and I&#x27;d like to restrict it to search in a manually-specified polygon (NOT to an existing area in OSM). The documentation mentions how to select region by polygon but it doesn&#x27;t tell me what to use instead of bbox-query to actually use that polygon. (My use-case: ...'''
date = "2014-05-26T14:54:00Z"
lastmod = "2014-07-27T09:56:00Z"
weight = 33478
keywords = [ "overpass", "polygon" ]
aliases = [ "/questions/33478" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass: restrict query to a manually-specified polygon](/questions/33478/overpass-restrict-query-to-a-manually-specified-polygon)

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
<span id="post-33478-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33478-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33478-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a simple Overpass XML query, and I'd like to restrict it to search in a manually-specified polygon (NOT to an existing area in OSM). The documentation mentions how to <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Select_region_by_polygon">select region by polygon</a> but it doesn't tell me what to use instead of <code>bbox-query</code> to actually <em>use</em> that polygon.</p>
<p>(My use-case: selecting e.g. all the lighthouses in mainland Britain. There are few enough lighthouses that it's OK to query such a big area, but the coast of Britain is far too complex to try and load into the Overpass interpreter so I drew a simplified outline.)</p>
<p>Here is my bbox query, which easily gets all the lighthouses in mainland Britain, but with a couple of extras from Ireland and France:</p>
<pre><code> {{key=man_made}}
 {{value=lighthouse}}
 &lt;osm-script output=&quot;json&quot;&gt;
   &lt;union&gt;
     &lt;query type=&quot;node&quot;&gt;
       &lt;has-kv k=&quot;{{key}}&quot; v=&quot;{{value}}&quot;/&gt;
       &lt;bbox-query w=&quot;-5.95459&quot; s=&quot;49.95122&quot; e=&quot;1.82373&quot; n=&quot;58.66551&quot;/&gt;
     &lt;/query&gt;
   &lt;/union&gt;
   &lt;print mode=&quot;body&quot;/&gt;
   &lt;recurse type=&quot;down&quot;/&gt;
   &lt;print mode=&quot;skeleton&quot;/&gt;
 &lt;/osm-script&gt;</code></pre>
<p>and here are my simplified coordinates, just manually drawn:</p>
<pre><code> &quot;50.0180967424 -5.7508254114  49.8977876566 -5.1328981537  50.9082889044 1.3228155649  51.2810475111 1.664301681  52.7126227103 1.9570040662  56.1970031699 -2.3893465301  57.6095221438 -1.5614591643  58.6835117066 -2.929773005  58.7133813218 -5.2524570036  57.7202251635 -6.0343506269  57.7570511223 -6.4712911811  57.3685045845 -6.9082317353  56.9193570841 -5.9883568844  56.8188049116 -5.9653600131  56.7573982738 -6.2873162109  56.686249528 -6.253314109  56.664139806 -6.0750883566  56.5375494332 -5.9256086933  56.4296138149 -5.6036524955  56.3118053314 -5.712887634  56.1199894834 -5.6381478024  55.907881817 -5.7818782478  55.7496536432 -5.6783923271  55.2809219893 -5.8681165151  55.3136533443 -5.4829189213  55.7043273009 -5.4024298718  55.7852302943 -5.2299533373  55.5029632207 -4.7872635653  54.8893427316 -5.3161916046  54.5806438387 -4.9194955751  54.6405756493 -4.0858589914  53.7730926517 -3.2407239721  53.4764508768 -3.528184863  53.5003957724 -4.7815143475  51.8269681676 -5.5979032777  51.4093186674 -4.9712385355  51.1215308565 -4.4078151893  50.1847866289 -5.8106243369  50.0180967424 -5.7508254114&quot;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 May '14, 14:54</strong></p>
<img src="https://secure.gravatar.com/avatar/cb99b2abaa73502ace0175863ca12b92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mcld&#39;s gravatar image" />
<p><span>mcld</span><br />
<span class="score" title="81 reputation points">81</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mcld has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33478" class="comments-container">
<span id="35229"></span>
<div id="comment-35229" class="comment">
<div id="post-35229-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why can't you use an existing area - or - combine several existing areas to the one you're looking for? Manually specifying coordinates looks a bit cumbersome to me.</p>
</div>
<div id="comment-35229-info" class="comment-info">
<span class="comment-age">(26 Jul '14, 22:46)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="35233"></span>
<div id="comment-35233" class="comment">
<div id="post-35233-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This works better for me. I could use an existing area, but the geometry for the UK has so much detail that the Overpass query takes a long time to run.</p>
</div>
<div id="comment-35233-info" class="comment-info">
<span class="comment-age">(27 Jul '14, 09:32)</span> <span class="comment-user userinfo">mcld</span>
</div>
</div>
<span id="35234"></span>
<div id="comment-35234" class="comment">
<div id="post-35234-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This query for United Kingdom based on areas takes just 20s. That's why I thought it's not really worth the effort: <a href="http://overpass-turbo.eu/s/4m3">http://overpass-turbo.eu/s/4m3</a></p>
</div>
<div id="comment-35234-info" class="comment-info">
<span class="comment-age">(27 Jul '14, 09:41)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="35235"></span>
<div id="comment-35235" class="comment">
<div id="post-35235-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That query does not do what I need. Thanks though.</p>
</div>
<div id="comment-35235-info" class="comment-info">
<span class="comment-age">(27 Jul '14, 09:47)</span> <span class="comment-user userinfo">mcld</span>
</div>
</div>
<span id="35236"></span>
<div id="comment-35236" class="comment">
<div id="post-35236-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Right. I didn't spend much time trying to find a matching relation, so the result includes more data than just mainland Britain. But that's absolutely expected behaviour (sorry for being a bit lazy on a Sunday morning :)</p>
<p>My point was: performance wise there's really no heavy penalty in using even a complex geometry originating from existing areas.</p>
</div>
<div id="comment-35236-info" class="comment-info">
<span class="comment-age">(27 Jul '14, 09:56)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-33478" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33478-form-container" class="comment-form-container">
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

<span id="33479"></span>

<div id="answer-container-33479" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33479-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mcld has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It <em>does</em> tell you what to use, but not as you seem to expect. Overpass has two different <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#The_languages">query language formats</a>: <em>XML</em> and its own language <em>QL</em>. The <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Select_region_by_polygon">select region by polygon example query</a> is written in QL but you seem to prefer the XML version. In that case just paste the code into the <a href="http://overpass-api.de/convert_form.html">Overpass API convert form</a> where you can convert between different formats. Converting the example query to XML will result in:</p>
<pre><code>&lt;osm-script&gt;
  &lt;union into=&quot;_&quot;&gt;
    &lt;polygon-query bounds=&quot;50.7 7.1 50.7 7.12 50.71 7.11&quot; into=&quot;_&quot;/&gt;
    &lt;recurse from=&quot;_&quot; into=&quot;_&quot; type=&quot;up&quot;/&gt;
  &lt;/union&gt;
  &lt;print from=&quot;_&quot; limit=&quot;&quot; mode=&quot;meta&quot; order=&quot;id&quot;/&gt;
&lt;/osm-script&gt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 May '14, 15:14</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-33479" class="comments-container">
&#10;</div>
<div id="comment-tools-33479" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33479-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33480"></span>

<div id="answer-container-33480" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33480-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Just to spell it out after <span><span>@scai</span></span> answered, here is exactly the Overpass XML that carries out my desired query:</p>
<pre><code>{{key=man_made}}
{{value=lighthouse}}
&lt;osm-script output=&quot;json&quot;&gt;
  &lt;union&gt;
    &lt;query type=&quot;node&quot;&gt;
      &lt;has-kv k=&quot;{{key}}&quot; v=&quot;{{value}}&quot;/&gt;
      &lt;polygon-query bounds=&quot;50.0180967424 -5.7508254114  49.8977876566 -5.1328981537  50.9082889044 1.3228155649  51.2810475111 1.664301681  52.7126227103 1.9570040662  56.1970031699 -2.3893465301  57.6095221438 -1.5614591643  58.6835117066 -2.929773005  58.7133813218 -5.2524570036  57.7202251635 -6.0343506269  57.7570511223 -6.4712911811  57.3685045845 -6.9082317353  56.9193570841 -5.9883568844  56.8188049116 -5.9653600131  56.7573982738 -6.2873162109  56.686249528 -6.253314109  56.664139806 -6.0750883566  56.5375494332 -5.9256086933  56.4296138149 -5.6036524955  56.3118053314 -5.712887634  56.1199894834 -5.6381478024  55.907881817 -5.7818782478  55.7496536432 -5.6783923271  55.2809219893 -5.8681165151  55.3136533443 -5.4829189213  55.7043273009 -5.4024298718  55.7852302943 -5.2299533373  55.5029632207 -4.7872635653  54.8893427316 -5.3161916046  54.5806438387 -4.9194955751  54.6405756493 -4.0858589914  53.7730926517 -3.2407239721  53.4764508768 -3.528184863  53.5003957724 -4.7815143475  51.8269681676 -5.5979032777  51.4093186674 -4.9712385355  51.1215308565 -4.4078151893  50.1847866289 -5.8106243369  50.0180967424 -5.7508254114&quot;/&gt;
    &lt;/query&gt;
  &lt;/union&gt;
  &lt;print mode=&quot;body&quot;/&gt;
  &lt;recurse type=&quot;down&quot;/&gt;
  &lt;print mode=&quot;skeleton&quot;/&gt;
&lt;/osm-script&gt;</code></pre>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 May '14, 15:19</strong></p>
<img src="https://secure.gravatar.com/avatar/cb99b2abaa73502ace0175863ca12b92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mcld&#39;s gravatar image" />
<p><span>mcld</span><br />
<span class="score" title="81 reputation points">81</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mcld has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 May '14, 15:20</strong> </span></p>
</div>
</div>
<div id="comments-container-33480" class="comments-container">
&#10;</div>
<div id="comment-tools-33480" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33480-form-container" class="comment-form-container">
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

