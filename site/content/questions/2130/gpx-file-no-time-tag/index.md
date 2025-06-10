+++
type = "question"
title = "GPX file : no time tag"
description = '''Hi, I have a problem in exporting my GPX file in openstreetmap : 2 minutes after sending the file, i got this in my mailbox &quot;Found no good GPX points in the input data. At least 75% of the trackpoints lacked a &amp;lt;time&amp;gt; tag.&quot; I checked the file, and there is actually no &amp;lt;time&amp;gt; tag.  Here is...'''
date = "2011-01-09T15:38:00Z"
lastmod = "2017-08-06T09:32:00Z"
weight = 2130
keywords = [ "error", "gpx", "time" ]
aliases = [ "/questions/2130" ]
osqa_answers = 6
osqa_accepted = false
+++

<div class="headNormal">

# [GPX file : no time tag](/questions/2130/gpx-file-no-time-tag)

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
<span id="post-2130-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2130-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-2130-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I have a problem in exporting my GPX file in openstreetmap : 2 minutes after sending the file, i got this in my mailbox</p>
<p>"Found no good GPX points in the input data. At least 75% of the trackpoints lacked a &lt;time&gt; tag."</p>
<p>I checked the file, and there is actually no &lt;time&gt; tag.<br />
Here is what my file looks like:</p>
<p><img src="http://dl.free.fr/gvgjQenCH.png" alt="alt text" /></p>
<p>Is anybody has the same problem ?</p>
<p>Thanks.</p>
<p>PS: I did some researches and I went on this link : <a href="https://bitbucket.org/lawgon/osmindia/src">https://bitbucket.org/lawgon/osmindia/src</a> but i wasn't able to run the scrpit (it tells me : "bogustimestamp takes precisely 3 parameters, you have given 1 parameters")</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jan '11, 15:38</strong></p>
<img src="https://secure.gravatar.com/avatar/15b17f6d0ce2c7a468245e05380d47fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bastoche&#39;s gravatar image" />
<p><span>Bastoche</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bastoche has no accepted answers">0%</span> </br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jun '11, 10:13</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span></p>
</div>
</div>
<div id="comments-container-2130" class="comments-container">
&#10;</div>
<div id="comment-tools-2130" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2130-form-container" class="comment-form-container">
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

6 Answers:

</div>

</div>

<span id="2146"></span>

<div id="answer-container-2146" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2146-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-2146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is because OSM requires a timestamp for all nodes in the GPX trace file. Why it is missing in your case depends on the tool you locally used with your GPS to generate this file. Sometimes it is a simple configuration hint to add the timestamp, sometimes it is not possible. A popular tool to generate GPX files for OSM is 'gpsbabel', you may have a look there.<br />
I also found a Python script which may help you fixing this issue <a href="https://bitbucket.org/lawgon/osmindia/src/tip/bogustimestamp.py">at this address</a>.<br />
</p>
<p>About the reason why the timestamp is required , I will quote Andy Robinson from the mailing-list : "The reason it's required is that it reduces the temptation for individuals to upload data in the GPX format that has not been gathered by a GPS. Of course that's not foolproof and it's not intended to be."</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jan '11, 12:53</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></br></p>
</div>
</div>
<div id="comments-container-2146" class="comments-container">
<span id="23992"></span>
<div id="comment-23992" class="comment">
<div id="post-23992-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"OSM requires a timestamp"</p>
<p>why? my tracks come from the software without timestamp and set the privacy settings, too close to publish without time ... it is not a good idea to have any gpx edit again</p>
<p>mfg jens</p>
</div>
<div id="comment-23992-info" class="comment-info">
<span class="comment-age">(04 Jul '13, 22:07)</span> <span class="comment-user userinfo">Jens_999</span>
</div>
</div>
<span id="23993"></span>
<div id="comment-23993" class="comment">
<div id="post-23993-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Requiring timestamps makes it more likely that the track is actually from a GPS device. And not just traced from Google Maps, or some other copyright source.</p>
<p>If you are concerned about privacy, then you can adjust the visibility of your GPS traces. <a href="http://wiki.openstreetmap.org/wiki/Visibility_of_GPS_traces">http://wiki.openstreetmap.org/wiki/Visibility_of_GPS_traces</a> ie set them as trackable, then they won't be linked to your account.</p>
<p>Or if you are really concerned about privacy, then don't upload any GPS tracks to OSM. You can still use them for editing the map - eg JOSM and ID allow you to load GPX files from your PC.</p>
</div>
<div id="comment-23993-info" class="comment-info">
<span class="comment-age">(05 Jul '13, 00:59)</span> <span class="comment-user userinfo">Vclaw</span>
</div>
</div>
<span id="23995"></span>
<div id="comment-23995" class="comment">
<div id="post-23995-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>...and P2.</p>
</div>
<div id="comment-23995-info" class="comment-info">
<span class="comment-age">(05 Jul '13, 07:11)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-2146" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2146-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2249"></span>

<div id="answer-container-2249" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2249-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2249-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-2249-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>With <code>xmlstarlet</code> you can add default timestamps:</p>
<p><code>xmlstarlet ed -N x=http://www.topografix.com/GPX/1/0 -s '//x:trkpt' -t elem -n time -v 1970-01-01T00:00:00Z track.gpx &gt; track-nulltime.gpx</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jan '11, 19:53</strong></p>
<img src="https://secure.gravatar.com/avatar/45b708b160b691d79e08415f24642ef0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Martin&#39;s gravatar image" />
<p><span>Martin</span><br />
<span class="score" title="75 reputation points">75</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Martin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2249" class="comments-container">
&#10;</div>
<div id="comment-tools-2249" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2249-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43164"></span>

<div id="answer-container-43164" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43164-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43164-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-43164-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I know this is an old question, but for others who need a solution, I have been working on a tool that will add timestamps to GPX files. It tries to preserve most of the GPX data, and lets you set a start time and an average speed:</p>
<p><a href="http://gotoes.org/strava/Add_Timestamps_To_GPX.php">http://gotoes.org/strava/Add_Timestamps_To_GPX.php</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 May '15, 07:46</strong></p>
<img src="https://secure.gravatar.com/avatar/451397e4047821b7e4e67a0f588fff9f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fulmar2&#39;s gravatar image" />
<p><span>fulmar2</span><br />
<span class="score" title="42 reputation points">42</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fulmar2 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43164" class="comments-container">
<span id="57473"></span>
<div id="comment-57473" class="comment">
<div id="post-57473-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This fixes the error if you want to import a gpx manually created, in the Garmin Connect application !!! Fixes! Fixes! Fixes! Thanks! Thanks! Thanks!</p>
<p>ps. Is possible to set the start and the end point?</p>
</div>
<div id="comment-57473-info" class="comment-info">
<span class="comment-age">(06 Aug '17, 09:32)</span> <span class="comment-user userinfo">Tarta</span>
</div>
</div>
</div>
<div id="comment-tools-43164" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43164-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2157"></span>

<div id="answer-container-2157" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2157-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2157-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-2157-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The GPS device i use is the "Tomtom Rider". I can't make the script work, i will try later, but by adding the timestamp by hand, it gave me a trace on OSM map.<br />
Thanks for your help anyway Pieren !</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jan '11, 18:28</strong></p>
<img src="https://secure.gravatar.com/avatar/15b17f6d0ce2c7a468245e05380d47fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bastoche&#39;s gravatar image" />
<p><span>Bastoche</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bastoche has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jan '11, 18:31</strong> </span></p>
</div>
</div>
<div id="comments-container-2157" class="comments-container">
<span id="2493"></span>
<div id="comment-2493" class="comment">
<div id="post-2493-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can send me your GPX and I'll test and fix the "script".</p>
</div>
<div id="comment-2493-info" class="comment-info">
<span class="comment-age">(27 Jan '11, 18:47)</span> <span class="comment-user userinfo">Martin</span>
</div>
</div>
<span id="2841"></span>
<div id="comment-2841" class="comment">
<div id="post-2841-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It works perfectly with xmlstarlet , thanks !</p>
</div>
<div id="comment-2841-info" class="comment-info">
<span class="comment-age">(09 Feb '11, 12:53)</span> <span class="comment-user userinfo">Bastoche</span>
</div>
</div>
</div>
<div id="comment-tools-2157" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2157-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2209"></span>

<div id="answer-container-2209" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2209-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-2209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>you can inspect or open a gpx file with windows note pad or a linux text editor, i've tried this on a windows tower system and a ubunto net book,These will then display type software that was used to create it and some other header info followed by a list of latitudes, longitudes,the date, the time when at that point,over and over again.I have set my garmin vista to one every second.I have downloaded and looked at someone else trace to compare to mine and theirs had the gps model in the header.I looked at some of my traces and found out where I was three years ago to the second.Osm needs the time stamps to prove they are genuine surveys.Hopefully you can read a problem or rejected trace and get a clue to what wrong.<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jan '11, 02:29</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span> </br></p>
</div>
</div>
<div id="comments-container-2209" class="comments-container">
&#10;</div>
<div id="comment-tools-2209" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2209-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2495"></span>

<div id="answer-container-2495" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2495-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2495-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-2495-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi! Looks like you used expertgps to create the gpx. Never just that software myself but I googled and I would be surprised if it is not able to convert keeping the timestamps. Try to search here: <a href="http://www.expertgps.com/support.asp"></a><a href="http://www.expertgps.com/support.asp"></a><a href="http://www.expertgps.com/support.asp">http://www.expertgps.com/support.asp</a></p>
<p>You could also try to use the editgpx plugin in JOSM. It allows for editing gpx and saving as anonymised time-stamps. Possibly it can also genereta the time-stamps when missing. See here: <a href="http://wiki.openstreetmap.org/wiki/JOSM/Plugins/EditGpx"></a><a href="http://wiki.openstreetmap.org/wiki/JOSM/Plugins/EditGpx"></a><a href="http://wiki.openstreetmap.org/wiki/JOSM/Plugins/EditGpx">http://wiki.openstreetmap.org/wiki/JOSM/Plugins/EditGpx</a></p>
<p>Happy mapping!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jan '11, 21:10</strong></p>
<img src="https://secure.gravatar.com/avatar/0db466a84d5c0ea91684afd01b97f5d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="geolr&#39;s gravatar image" />
<p><span>geolr</span><br />
<span class="score" title="70 reputation points">70</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="geolr has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2495" class="comments-container">
&#10;</div>
<div id="comment-tools-2495" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2495-form-container" class="comment-form-container">
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

