+++
type = "question"
title = "Loading an osm file with Halycon/Potlatch 2"
description = '''Hi all, I am trying to make a standalone flash OSM viewer, and had no problems compiling etc. I am stuck on what flash variables to use to set the path to load a osm file, instead of loading from the OSM api. I have found on potlatch 2 related websites that loading from an OSM file is a feature, but...'''
date = "2011-03-04T05:07:00Z"
lastmod = "2011-03-05T12:21:00Z"
weight = 3509
keywords = [ "potlatch2", "flash", "halcyon" ]
aliases = [ "/questions/3509" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Loading an osm file with Halycon/Potlatch 2](/questions/3509/loading-an-osm-file-with-halyconpotlatch-2)

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
<span id="post-3509-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3509-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3509-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I am trying to make a standalone flash OSM viewer, and had no problems compiling etc. I am stuck on what flash variables to use to set the path to load a osm file, instead of loading from the OSM api. I have found on potlatch 2 related websites that loading from an OSM file is a feature, but how do I do it? There doesn't seem to be any documentation anywhere on what parameters can be passed in. Thanks!</p>
<pre><code>fo.addVariable(&quot;lat&quot;,51.875);
fo.addVariable(&quot;lon&quot;,-1.482);
fo.addVariable(&quot;zoom&quot;,14);
fo.addVariable(&quot;api&quot;,&quot;http://www.openstreetmap.org/api/0.6/&quot;);
fo.addVariable(&quot;policy&quot;,&quot;http://www.openstreetmap.org/api/crossdomain.xml&quot;);
fo.addVariable(&quot;connection&quot;,&quot;AMF&quot;);
fo.addVariable(&quot;responder&quot;,&quot;respond&quot;);
fo.addVariable(&quot;tileurl&quot;,&quot;http://npe.openstreetmap.org/$z/$x/$y.png&quot;);
fo.addVariable(&quot;style&quot;,&quot;stylesheets/openskimap.css&quot;);
fo.addVariable(&quot;show_debug&quot;,&quot;true&quot;);
fo.write(&quot;map&quot;);</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-potlatch2" rel="tag" title="see questions tagged &#39;potlatch2&#39;">potlatch2</span> <span class="post-tag tag-link-flash" rel="tag" title="see questions tagged &#39;flash&#39;">flash</span> <span class="post-tag tag-link-halcyon" rel="tag" title="see questions tagged &#39;halcyon&#39;">halcyon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Mar '11, 05:07</strong></p>
<img src="https://secure.gravatar.com/avatar/3a5c89275037ff2627640835b33e9483?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wbski&#39;s gravatar image" />
<p><span>wbski</span><br />
<span class="score" title="146 reputation points">146</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wbski has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-3509" class="comments-container">
&#10;</div>
<div id="comment-tools-3509" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3509-form-container" class="comment-form-container">
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

<span id="3516"></span>

<div id="answer-container-3516" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3516-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3516-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-3516-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wbski has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to set the connection type to "OSM" instead of "AMF", and you need to name your files with the bounding box that they cover.</p>
<p>For example,</p>
<pre><code> fo.addVariable(&quot;api&quot;,&quot;http://127.0.0.1/~richard/potlatch2&quot;);       // base URL
 fo.addVariable(&quot;connection&quot;,&quot;OSM&quot;);
 fo.addVariable(&quot;files&quot;,&quot;-1.5_-1.4_52.1_52.2.osm&quot;);</code></pre>
<p>You can provide a comma-separated list of .osm files if you have more than one. Halcyon will then load from whichever files are relevant for the area that is being shown. You'll also need a crossdomain.xml file to authorise flash to load the files - put it in the same directory or a parent directory, and load it with the "policy" setting.</p>
<p>The "OSM" connection isn't a very well tested part of the code, so you may find a few bugs with it. If you find any bugs please report them on <a href="http://trac.openstreetmap.org">trac</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '11, 09:49</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Mar '11, 09:56</strong> </span></p>
</div>
</div>
<div id="comments-container-3516" class="comments-container">
<span id="3517"></span>
<div id="comment-3517" class="comment">
<div id="post-3517-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What do you mean with: '"OSM" connection isn't a very well tested part of the code' care to expand?</p>
</div>
<div id="comment-3517-info" class="comment-info">
<span class="comment-age">(04 Mar '11, 09:57)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
<span id="3518"></span>
<div id="comment-3518" class="comment">
<div id="post-3518-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I mean that part of the code that loads standalone OSM files isn't very well tested - I'm not aware of anyone using it other than RichardF quite some time ago. The "XML" connection type, however, is used thoroughly so we know that it works well.</p>
</div>
<div id="comment-3518-info" class="comment-info">
<span class="comment-age">(04 Mar '11, 11:07)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
<span id="3526"></span>
<div id="comment-3526" class="comment">
<div id="post-3526-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That works fine. Is there any way I could do this without renaming all my OSM files? After all, the bounding box data is already at the top of the osm file: &lt;bound box="49.34000,-123.26000,49.46000,-123.14000" origin="Osmosis SNAPSHOT-rexported"/&gt; I could easily pass in the bbox through the flash variables as well. Thanks!!</p>
</div>
<div id="comment-3526-info" class="comment-info">
<span class="comment-age">(04 Mar '11, 16:42)</span> <span class="comment-user userinfo">wbski</span>
</div>
</div>
<span id="3527"></span>
<div id="comment-3527" class="comment">
<div id="post-3527-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hmm, I think I might have found a bug.. fo.addVariable("style","stylesheets/simple.css"); Doesn't load the mapcss.. If I just paste the css into the textbox on the side (same html as geowiki), it works fine. It doesn't seem to load on the geowiki page either, until someone clicks refresh css.. <a href="http://www.geowiki.com/halcyon/">http://www.geowiki.com/halcyon/</a> Should I file a bug or do you think I am doing something wrong here?</p>
</div>
<div id="comment-3527-info" class="comment-info">
<span class="comment-age">(04 Mar '11, 17:01)</span> <span class="comment-user userinfo">wbski</span>
</div>
</div>
<span id="3570"></span>
<div id="comment-3570" class="comment">
<div id="post-3570-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Suggest you file a bug.</p>
</div>
<div id="comment-3570-info" class="comment-info">
<span class="comment-age">(05 Mar '11, 12:21)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-3516" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3516-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3515"></span>

<div id="answer-container-3515" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3515-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3515-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3515-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I found an option called <code>files</code> in P2 code, it seems to take a comma seperated list of.osm files.</p>
<p>Other options I found in P2 source:</p>
<pre><code>api
connection
files
force_auth
gpx
gpx_url
locale
maximise_function
minimise_function
move_function
nocache
oauth_access_url
oauth_auth_url
oauth_consumer_key
oauth_consumer_secret
oauth_policy
oauth_request_url
oauth_token
oauth_token_secret
policy
responder
serverName
show_debug
show_help
site_name
style
tile_resolution
tileurl</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '11, 09:24</strong></p>
<img src="https://secure.gravatar.com/avatar/dd3858f5f89f5a6b738f9dbe59824440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emj&#39;s gravatar image" />
<p><span>emj</span><br />
<span class="score" title="2024 reputation points"><span>2.0k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emj has 11 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Mar '11, 09:58</strong> </span></p>
</div>
</div>
<div id="comments-container-3515" class="comments-container">
&#10;</div>
<div id="comment-tools-3515" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3515-form-container" class="comment-form-container">
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

