+++
type = "question"
title = "wget to nominatim URL: Unable to establish SSL connection."
description = '''I have possibly the same problem as that older question; I copied the url to a windows 10 installation. result:  wget &quot;http://nominatim.openstreetmap.org/reverse?format=xml&amp;amp;limit=1&amp;amp;addressdetails=1&amp;amp;zoom=18&amp;amp;email=&amp;amp;lat=-0.24136&amp;amp;lon=98.48281&quot;  --21:36:57-- http://nominatim.opens...'''
date = "2018-11-27T20:44:00Z"
lastmod = "2018-11-28T07:38:00Z"
weight = 66940
keywords = [ "wget", "nominatim" ]
aliases = [ "/questions/66940" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wget to nominatim URL: Unable to establish SSL connection.](/questions/66940/wget-to-nominatim-url-unable-to-establish-ssl-connection)

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
<span id="post-66940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66940-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have possibly the same problem as <a href="https://help.openstreetmap.org/questions/45261/error-nomination-geocode-with-wget">that older question</a>; I copied the url to a windows 10 installation. result:</p>
<pre><code>  wget &quot;http://nominatim.openstreetmap.org/reverse?format=xml&amp;limit=1&amp;addressdetails=1&amp;zoom=18&amp;email=&amp;lat=-0.24136&amp;lon=98.48281&quot;
    --21:36:57--  http://nominatim.openstreetmap.org/reverse?format=xml&amp;limit=1&amp;addressdetails=1&amp;zoom=18&amp;email=&amp;lat=-0.24136&amp;lon=98.48281
               =&gt; `reverse@format=xml&amp;limit=1&amp;addressdetails=1&amp;zoom=18&amp;email=&amp;lat=-0.24136&amp;lon=98.48281&#39;
    Resolving nominatim.openstreetmap.org... done.
    Connecting to nominatim.openstreetmap.org[130.117.76.9]:80... connected.
    HTTP request sent, awaiting response... 301 Moved Permanently
    Location: https://nominatim.openstreetmap.org/reverse?format=xml&amp;limit=1&amp;addressdetails=1&amp;zoom=18&amp;email=&amp;lat=-0.24136&amp;lon=98.48281 [following]
    --21:36:57--  https://nominatim.openstreetmap.org/reverse?format=xml&amp;limit=1&amp;addressdetails=1&amp;zoom=18&amp;email=&amp;lat=-0.24136&amp;lon=98.48281
               =&gt; `reverse@format=xml&amp;limit=1&amp;addressdetails=1&amp;zoom=18&amp;email=&amp;lat=-0.24136&amp;lon=98.48281&#39;
    Connecting to nominatim.openstreetmap.org[130.117.76.9]:443... connected.
&#10;    Unable to establish SSL connection.
&#10;    Unable to establish SSL connection.</code></pre>
<p>I also tried direct https:</p>
<pre><code>wget &quot;https://nominatim.openstreetmap.org/reverse?format=xml&amp;limit=1&amp;addressdetails=1&amp;zoom=18&amp;email=&amp;lat=-0.24136&amp;lon=98.48281&quot;
--21:39:27--  https://nominatim.openstreetmap.org/reverse?format=xml&amp;limit=1&amp;addressdetails=1&amp;zoom=18&amp;email=&amp;lat=-0.24136&amp;lon=98.48281
           =&gt; `reverse@format=xml&amp;limit=1&amp;addressdetails=1&amp;zoom=18&amp;email=&amp;lat=-0.24136&amp;lon=98.48281&#39;
Resolving nominatim.openstreetmap.org... done.
Connecting to nominatim.openstreetmap.org[130.117.76.9]:443... connected.
&#10;Unable to establish SSL connection.
&#10;Unable to establish SSL connection.</code></pre>
<p>What is the problem here? In a browser on the same machine the same URls succseed.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wget" rel="tag" title="see questions tagged &#39;wget&#39;">wget</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Nov '18, 20:44</strong></p>
<img src="https://secure.gravatar.com/avatar/7b22f0b3304066470193db063a024ea2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stefanwoe&#39;s gravatar image" />
<p><span>stefanwoe</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stefanwoe has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> converted to question <strong>27 Nov '18, 20:54</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-66940" class="comments-container">
<span id="66946"></span>
<div id="comment-66946" class="comment">
<div id="post-66946-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The <a href="https://www.gnu.org/software/wget/manual/wget.html#Logging-and-Input-File-Options">GNU Wget documentation</a> says you can add <code>--debug</code> to the wget command line to get more detailed debugging information. Does this give any useful information? Please edit your question to include the result it shows when you try this.</p>
</div>
<div id="comment-66946-info" class="comment-info">
<span class="comment-age">(28 Nov '18, 03:43)</span> <span class="comment-user userinfo">Krubo</span>
</div>
</div>
</div>
<div id="comment-tools-66940" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66940-form-container" class="comment-form-container">
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

<span id="66941"></span>

<div id="answer-container-66941" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66941-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66941-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-66941-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I guess you do not have the same problem. Rather your wget cannot establish the SSL connection - which may be due to a variety of reasons. Default output of wget is already verbose mode, so we cannot get more details of the logging.</p>
<p>I <em>guess</em> the problem may be that your wget does not have the right CA certificate available. In my wget output (on linux) I see an additional line <code>Loaded CA certificate '/etc/ssl/certs/ca-certificates.crt'</code>. I would have expected a different error message from wget, though. Can you successfully use wget with other https URLs?</p>
<p>Anyway: Do not use Windows! ;-)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Nov '18, 21:04</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Nov '18, 21:10</strong> </span></p>
</div>
</div>
<div id="comments-container-66941" class="comments-container">
<span id="66942"></span>
<div id="comment-66942" class="comment">
<div id="post-66942-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello aseerel4c26, thanks for your answer.</p>
<p>My original goal is it, to get nominatim access from a windows applications, where users can search for places etc. We are doing this since many years quite well with other providers (with google, bing, mapquest etc.) and i wanted to add nominatim as well. This is a c++ application on windows using boost::asio for https / https access. https works well for all other services. But using nominatim i get the same results as using wget.</p>
<p>Any hint what i can do here?</p>
<p>And yes: wget works coorect with other https URLs</p>
</div>
<div id="comment-66942-info" class="comment-info">
<span class="comment-age">(27 Nov '18, 21:12)</span> <span class="comment-user userinfo">stefanwoe</span>
</div>
</div>
<span id="66943"></span>
<div id="comment-66943" class="comment">
<div id="post-66943-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's nice to add nominatim. Nominatim has a Let's encrypt cert, just to rule out this specialty (in case your CA certs are a bit outdated), try <code>--no-check-certificate</code> as additional parameter for wget.</p>
<p>Side note: Please obey <a href="https://operations.osmfoundation.org/policies/nominatim/">https://operations.osmfoundation.org/policies/nominatim/</a> .</p>
<p>Just by chance: if you already tried many many times from your IP your access may (although I would expect the block to happen after the establishment of the SSL connection) be blocked due to policy violation. Try to set a useful user agent for wget'S request - maybe your mail address or your application's (unique) name.</p>
</div>
<div id="comment-66943-info" class="comment-info">
<span class="comment-age">(27 Nov '18, 21:24)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="66944"></span>
<div id="comment-66944" class="comment">
<div id="post-66944-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i use wget from unixutils (GNU Wget 1.8.2) it does not accept a parameter like --no-check-certificate. Also in our application we do not check any certificates.</p>
<p>I doubt that i was blocked - all calls in the browser succeed without problems.</p>
</div>
<div id="comment-66944-info" class="comment-info">
<span class="comment-age">(27 Nov '18, 21:56)</span> <span class="comment-user userinfo">stefanwoe</span>
</div>
</div>
<span id="66947"></span>
<div id="comment-66947" class="comment">
<div id="post-66947-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>wget 1.8.2 is from 2002. Due to its age it can't have support for TLS &gt;= 1.1. All previous TLS/SSL versions are outdated and insecure. Update your software for your own sake.</p>
</div>
<div id="comment-66947-info" class="comment-info">
<span class="comment-age">(28 Nov '18, 07:23)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="66949"></span>
<div id="comment-66949" class="comment">
<div id="post-66949-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ouch! I use GNU Wget 1.19.5 -- your version is (according to <a href="https://ftp.gnu.org/gnu/wget/">https://ftp.gnu.org/gnu/wget/</a> ) from year 2002. That's quite stone age - in 2002 TLS 1.0 was current and possibly the highest TLS version supported by your wget version. According to <a href="https://www.ssllabs.com/ssltest/analyze.html?d=nominatim.openstreetmap.org&amp;s=130.117.76.9&amp;latest">ssllabs</a> the nominatim server would <em>still</em> support TLS 1.0. However, please update your wget (and then post the debug log as suggested by Krubo).</p>
</div>
<div id="comment-66949-info" class="comment-info">
<span class="comment-age">(28 Nov '18, 07:38)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-66941" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66941-form-container" class="comment-form-container">
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

