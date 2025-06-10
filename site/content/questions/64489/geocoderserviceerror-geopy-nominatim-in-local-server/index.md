+++
type = "question"
title = "GeocoderServiceError Geopy Nominatim in Local Server"
description = '''I did my own OpenStreetMap local server(to avoid the online limits) with Nominatim and it&#x27;s working ok through the webpage(localhost/nominatim). But when I try to collect geocodes (same that works well on the webpage) and after some number of requests the server shows this error: Traceback (most rec...'''
date = "2018-07-02T23:07:00Z"
lastmod = "2018-07-02T23:27:00Z"
weight = 64489
keywords = [ "geopy", "nominatim" ]
aliases = [ "/questions/64489" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [GeocoderServiceError Geopy Nominatim in Local Server](/questions/64489/geocoderserviceerror-geopy-nominatim-in-local-server)

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
<span id="post-64489-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64489-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64489-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I did my own OpenStreetMap local server(to avoid the online limits) with Nominatim and it's working ok through the webpage(localhost/nominatim). But when I try to collect geocodes (same that works well on the webpage) and after some number of requests the server shows this error:</p>
<pre><code>Traceback (most recent call last):
&#10;  File &quot;&lt;ipython-input-65-1a4379f0657b&gt;&quot;, line 4, in &lt;module&gt;
    print (nom.geocode(row[&#39;location&#39;]))
&#10;  File &quot;/Users/murianribeiro/anaconda3/lib/python3.6/site-packages/geopy/geocoders/osm.py&quot;, line 236, in geocode
    self._call_geocoder(url, timeout=timeout), exactly_one
&#10;  File &quot;/Users/murianribeiro/anaconda3/lib/python3.6/site-packages/geopy/geocoders/base.py&quot;, line 288, in _call_geocoder
    raise GeocoderServiceError(message)
&#10;GeocoderServiceError: HTTP Error 500: Internal Server Error</code></pre>
<p>I tried to put timeout in my code, but I am still facing the same problem.</p>
<p>My actual code is more or less like this:</p>
<pre><code>from geopy.geocoders import Nominatim
nom = Nominatim(domain=&#39;192.168.1.214/nominatim&#39;, scheme=&#39;http&#39;, timeout=3) #tried with different timeouts
df1[&quot;Coordinates&quot;]=df1[&quot;location&quot;].apply(nom.geocode)</code></pre>
<p>Someone know how to solve this?</p>
<p>Thanks ;)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geopy" rel="tag" title="see questions tagged &#39;geopy&#39;">geopy</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jul '18, 23:07</strong></p>
<img src="https://secure.gravatar.com/avatar/743a6b18621cbd268e6d8a7963571f4f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MurianRibeiro&#39;s gravatar image" />
<p><span>MurianRibeiro</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MurianRibeiro has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64489" class="comments-container">
<span id="64490"></span>
<div id="comment-64490" class="comment">
<div id="post-64490-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><code>Internal Server Error</code> doesn't look python related. On your server check the logfile, likely <code>/var/log/apache2/error.log</code></p>
</div>
<div id="comment-64490-info" class="comment-info">
<span class="comment-age">(02 Jul '18, 23:27)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-64489" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64489-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

