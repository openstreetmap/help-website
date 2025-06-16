+++
type = "question"
title = "Nominatim installation Problem"
description = '''I want to embed Search box on My Own Map on my tile server. i have followed reference from http://open.mapquestapi.com/npi/ to install nominatim pre index. but i have problem when execute command : ../utils/setup.php --create-db --create-functions --create-minimal-tables  Create DB Create DB (2) PHP...'''
date = "2011-12-30T10:21:00Z"
lastmod = "2012-01-03T14:54:00Z"
weight = 9702
keywords = [ "mapquest", "npi", "nominatim", "postgresql" ]
aliases = [ "/questions/9702" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim installation Problem](/questions/9702/nominatim-installation-problem)

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
<span id="post-9702-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9702-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9702-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to embed Search box on My Own Map on my tile server. i have followed reference from <a href="http://open.mapquestapi.com/npi/">http://open.mapquestapi.com/npi/</a> to install nominatim pre index. but i have problem when execute command :</p>
<pre><code>../utils/setup.php --create-db --create-functions --create-minimal-tables
&#10;Create DB
Create DB (2)
PHP Warning:  log() expects parameter 1 to be double, string given in /home/user/Map/src/nominatim/lib/
lib.php on line 6
unable to find /usr/share/postgresql/9.0/contrib/_int.sql</code></pre>
<p>I use postgres 8.4 on my machine.Error message is like that script wrong read a postgresql folder. How to solve this issue ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapquest" rel="tag" title="see questions tagged &#39;mapquest&#39;">mapquest</span> <span class="post-tag tag-link-npi" rel="tag" title="see questions tagged &#39;npi&#39;">npi</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Dec '11, 10:21</strong></p>
<img src="https://secure.gravatar.com/avatar/3b1d427556c3521f0b264e23ede364fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MIftakhul%20Anwar&#39;s gravatar image" />
<p><span>MIftakhul Anwar</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MIftakhul Anwar has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9702" class="comments-container">
<span id="9737"></span>
<div id="comment-9737" class="comment">
<div id="post-9737-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OMG, log is for logarithm. <a href="http://php.net/manual/en/function.log.php">http://php.net/manual/en/function.log.php</a></p>
</div>
<div id="comment-9737-info" class="comment-info">
<span class="comment-age">(02 Jan '12, 03:25)</span> <span class="comment-user userinfo">h4ck3rm1k3</span>
</div>
</div>
<span id="9738"></span>
<div id="comment-9738" class="comment">
<div id="post-9738-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>try again without --create-db</p>
</div>
<div id="comment-9738-info" class="comment-info">
<span class="comment-age">(02 Jan '12, 04:04)</span> <span class="comment-user userinfo">h4ck3rm1k3</span>
</div>
</div>
</div>
<div id="comment-tools-9702" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9702-form-container" class="comment-form-container">
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

<span id="9703"></span>

<div id="answer-container-9703" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9703-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9703-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9703-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You will have to change the value of <code>CONST_Path_Postgresql_Contrib</code> in your <code>settings/settings.php</code> file to point to the directory where your <code>_int.sql</code> resides. Make sure to install the proper PostgreSQL contrib package first (e.g. <code>postgresql-contrib-8.4</code> on Ubuntu Lucid).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Dec '11, 10:28</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-9703" class="comments-container">
<span id="9736"></span>
<div id="comment-9736" class="comment">
<div id="post-9736-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, i have change that value on setting.php.</p>
<p>i have execute again</p>
<p>../utils/setup.php --create-db --create-functions --create-minimal-tables</p>
<p>But on end of line of output, i have got warning like bellow .</p>
<p>[output]</p>
<pre><code>INSERT 0 1
INSERT 0 1
INSERT 0 1
...
SET
SET
CREATE TABLE
SET
SET
SET
SET
SET
SET
SET
SET
CREATE TABLE
ALTER TABLE
Functions
PHP Warning:  log() expects parameter 1 to be double, string given in /home/user/Map/src/nominatim/lib/lib.php on line 6
nominatim module not built</code></pre>
<p>i'm running script as user which have role on postgresql but not as postgres. is it problem ?</p>
<p>This is line 6 on lib.php</p>
<pre><code> function fail($sError, $sUserError = false)
    {
            if (!$sUserError) $sUserError = $sError;
            log(&#39;ERROR:&#39;.$sError);  //line 6
            echo $sUserError.&quot;\n&quot;;
            exit;
    }</code></pre>
</div>
<div id="comment-9736-info" class="comment-info">
<span class="comment-age">(02 Jan '12, 02:13)</span> <span class="comment-user userinfo">MIftakhul Anwar</span>
</div>
</div>
<span id="9777"></span>
<div id="comment-9777" class="comment">
<div id="post-9777-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have continuing step and now i have on generating website step.</p>
<p>I have execute this script as described in reference: ../setup.php --create-website /var/www/html</p>
<p>NOw i have publish it on <a href="http://www.osmosa.net/search">http://www.osmosa.net/search</a> But when i access web, i get error on apache log.</p>
<pre><code>[Tue Jan 03 21:27:02 2012] [error] [client 118.137.0.31] PHP Notice:  Undefined index: PATH_INFO in /home/user/Map/src/nominatim/website/search.php on line 95
&#10;[Tue Jan 03 21:27:02 2012] [error] [client 118.137.0.31] PHP Notice:  Use of undefined constant CONST_Search_AreaPolygons - assumed &#39;CONST_Search_AreaPolygons&#39; in /home/user/Map/src/nominatim/lib/template/search-html.php on line 327</code></pre>
<p>i have checked on /home/user/Map/src/nominatim/website/search.php on line 95, i get script bellow :</p>
<pre><code> $sQuery = (isset($_GET[&#39;q&#39;])?trim($_GET[&#39;q&#39;]):&#39;&#39;);
    if (!$sQuery &amp;&amp; $_SERVER[&#39;PATH_INFO&#39;] &amp;&amp; $_SERVER[&#39;PATH_INFO&#39;][0] == &#39;/&#39;)  /* &gt;&gt; line 95
    {
            $sQuery = substr($_SERVER[&#39;PATH_INFO&#39;], 1);
&#10;            // reverse order of &#39;/&#39; seperated string
            $aPhrases = explode(&#39;/&#39;, $sQuery);
            $aPhrases = array_reverse($aPhrases); 
            $sQuery = join(&#39;, &#39;,$aPhrases);
    }</code></pre>
<p>Then i check on /home/user/Map/src/nominatim/lib/template/search-html.php line 327.and i get this line one</p>
<pre><code>&lt;?php if (CONST_Search_AreaPolygons) { ?&gt;&lt;td style=&quot;width:100px;&quot;&gt;&lt;input type=&quot;checkbox&quot; value=&quot;1&quot; name=&quot;polygon&quot; &lt;?php if ($bSh$
&lt;td style=&quot;text-align:right;&quot;&gt;Data: &lt;?php echo $sDataDate; ?&gt;&lt;/td&gt;
&lt;td style=&quot;text-align:right;&quot;&gt;
&lt;a href=&quot;https://wiki.openstreetmap.org/wiki/Nominatim&quot; target=&quot;_blank&quot;&gt;Documentation&lt;/a&gt; | &lt;a href=&quot;https://wiki.openstreetmap.org/wiki/Nominatim/FAQ&quot; 
target=&quot;_blank&quot;&gt;FAQ&lt;/a&gt;&lt;/td&gt;</code></pre>
<p>&lt;?php }</p>
<p>Then i see on nominatim folder /setting/setting.php and i get that constanta have value :</p>
<p>@define('CONST_Search_AreaPolygons_Enabled', true);</p>
<p>how i can set PATH_INFO which now is undefined ?</p>
<p>Thanks</p>
</div>
<div id="comment-9777-info" class="comment-info">
<span class="comment-age">(03 Jan '12, 14:54)</span> <span class="comment-user userinfo">MIftakhul Anwar</span>
</div>
</div>
</div>
<div id="comment-tools-9703" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9703-form-container" class="comment-form-container">
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

