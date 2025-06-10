+++
type = "question"
title = "Given a lat/lon, how do I find the precise position on the tile?"
description = '''Given a latitude and longitude, I can find the correct tile number - but how do I find the correct position (in pixel) on the tile?'''
date = "2010-09-07T08:14:00Z"
lastmod = "2023-01-09T11:19:00Z"
weight = 747
keywords = [ "tile", "latitude", "calulation", "longitude", "position" ]
aliases = [ "/questions/747" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Given a lat/lon, how do I find the precise position on the tile?](/questions/747/given-a-latlon-how-do-i-find-the-precise-position-on-the-tile)

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
<span id="post-747-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-747-score" class="post-score" title="current number of votes">
10
</div>
<span id="post-747-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
4
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Given a latitude and longitude, I can find the correct tile number - but how do I find the correct position (in pixel) on the tile?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tile" rel="tag" title="see questions tagged &#39;tile&#39;">tile</span> <span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span> <span class="post-tag tag-link-calulation" rel="tag" title="see questions tagged &#39;calulation&#39;">calulation</span> <span class="post-tag tag-link-longitude" rel="tag" title="see questions tagged &#39;longitude&#39;">longitude</span> <span class="post-tag tag-link-position" rel="tag" title="see questions tagged &#39;position&#39;">position</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Sep '10, 08:14</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>17 Feb '11, 14:03</strong> </span></p>
</div>
</div>
<div id="comments-container-747" class="comments-container">
<span id="3135"></span>
<div id="comment-3135" class="comment">
<div id="post-3135-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>related to <a href="http://help.openstreetmap.org/questions/2687/coordinates-to-pixels-based-on-zoom">the question about coordinates to pixels</a></p>
</div>
<div id="comment-3135-info" class="comment-info">
<span class="comment-age">(17 Feb '11, 14:37)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
</div>
<div id="comment-tools-747" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-747-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="748"></span>

<div id="answer-container-748" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-748-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-748-score" class="post-score" title="current number of votes">
12
</div>
<span id="post-748-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When you calulate the tile number according to <a href="http://wiki.openstreetmap.org/wiki/Tilenames">the wiki</a> you will actually get a floating point number.</p>
<p>The integer part indicates which tile you are (or should be) looking at.</p>
<p>The fractional part indicates the position within the tile. As a tile is 256 pixel wide, multiplying the fractional part with 256 will give you the pixel position from the top left.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Sep '10, 08:16</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Sep '10, 10:19</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span></p>
</div>
</div>
<div id="comments-container-748" class="comments-container">
<span id="82162"></span>
<div id="comment-82162" class="comment">
<div id="post-82162-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you show a detailed example? for example we have lat : 36 lon: 6 we create square earth map with real scale in autocad how we can find the position x,y of the coordinates in the map? i don't see an example or a formula in the wiki</p>
</div>
<div id="comment-82162-info" class="comment-info">
<span class="comment-age">(14 Oct '21, 06:27)</span> <span class="comment-user userinfo">Seghier</span>
</div>
</div>
</div>
<div id="comment-tools-748" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-748-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="749"></span>

<div id="answer-container-749" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-749-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-749-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-749-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you just want to see the position on the map, you can use <em>mlat</em> and <em>mlon</em> to get a <a href="http://www.openstreetmap.org/?mlat=48.03611&amp;mlon=10.55885&amp;zoom=16&amp;layers=M">marker</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Sep '10, 13:39</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-749" class="comments-container">
<span id="82163"></span>
<div id="comment-82163" class="comment">
<div id="post-82163-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>what you mean by mlat and mlon? where is the formula?</p>
</div>
<div id="comment-82163-info" class="comment-info">
<span class="comment-age">(14 Oct '21, 06:29)</span> <span class="comment-user userinfo">Seghier</span>
</div>
</div>
</div>
<div id="comment-tools-749" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-749-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8971"></span>

<div id="answer-container-8971" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8971-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8971-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8971-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've written the following conversion functions to convert from Lat/Long coordinates to OSM pixel x,y coordinates for a given zoom level.</p>
<pre><code>Friend Sub LatLongToPixelXYOSM(ByVal latitude As Double, ByVal longitude As Double, ByVal zoomLevel As Integer, ByRef pixelX As Integer, ByRef pixelY As Integer)
        Dim MinLatitude = -85.05112878
        Dim MaxLatitude = 85.05112878
        Dim MinLongitude = -180
        Dim MaxLongitude = 180
        Dim mapSize = Math.Pow(2, zoomLevel) * 256
&#10;        latitude = Clip(latitude, MinLatitude, MaxLatitude)
        longitude = Clip(longitude, MinLongitude, MaxLongitude)
&#10;        Dim p As PointF = New Point()
        p.X = CSng((longitude + 180.0) / 360.0 * (1 &lt;&lt; zoomLevel))
        p.Y = CSng((1.0 - Math.Log(Math.Tan(latitude * Math.PI / 180.0) + 1.0 / Math.Cos(toRadians(latitude))) / Math.PI) / 2.0 * (1 &lt;&lt; zoomLevel))
&#10;        Dim tilex As Integer = CInt(Math.Truncate(p.X))
        Dim tiley As Integer = CInt(Math.Truncate(p.Y))
        pixelX = ClipByRange((tilex * 256) + ((p.X - tilex) * 256), mapSize - 1)
        pixelY = ClipByRange((tiley * 256) + ((p.Y - tiley) * 256), mapSize - 1)
    End Sub
&#10;Friend Sub PixelXYToLatLongOSM(ByVal pixelX As Integer, ByVal pixelY As Integer, ByVal zoomLevel As Integer, ByRef latitude As Double, ByRef longitude As Double)
        Dim mapSize = Math.Pow(2, zoomLevel) * 256
        Dim tileX As Integer = Math.Truncate(pixelX / 256)
        Dim tileY As Integer = Math.Truncate(pixelY / 256)
&#10;        Dim p As PointF = New Point()
        Dim n As Double = Math.PI - ((2.0 * Math.PI * (ClipByRange(pixelY, mapSize - 1) / 256)) / Math.Pow(2.0, zoomLevel))
&#10;        longitude = CSng(((ClipByRange(pixelX, mapSize - 1) / 256) / Math.Pow(2.0, zoomLevel) * 360.0) - 180.0)
        latitude = CSng(180.0 / Math.PI * Math.Atan(Math.Sinh(n)))
    End Sub
&#10;Private Function ClipByRange(ByVal n As Double, ByVal range As Double)
        Return n Mod range
End Function
&#10;Private Function Clip(ByVal n As Double, ByVal minValue As Double, ByVal maxValue As Double)
      Return Math.Min(Math.Max(n, minValue), maxValue)
End Function</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Nov '11, 10:27</strong></p>
<img src="https://secure.gravatar.com/avatar/388bd8953c15a6093aae795c7991145e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johnmeilak&#39;s gravatar image" />
<p><span>johnmeilak</span><br />
<span class="score" title="25 reputation points">25</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johnmeilak has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8971" class="comments-container">
&#10;</div>
<div id="comment-tools-8971" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8971-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86461"></span>

<div id="answer-container-86461" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86461-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86461-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86461-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the editor, press CTRL+SHIFT+L to display the Location Panel.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jan '23, 11:19</strong></p>
<img src="https://secure.gravatar.com/avatar/63bf3553cfc4f167abe24eaad9deaad1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joper34&#39;s gravatar image" />
<p><span>joper34</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joper34 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jan '23, 11:24</strong> </span></p>
</div>
</div>
<div id="comments-container-86461" class="comments-container">
&#10;</div>
<div id="comment-tools-86461" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86461-form-container" class="comment-form-container">
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

