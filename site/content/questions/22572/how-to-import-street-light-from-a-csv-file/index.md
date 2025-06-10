+++
type = "question"
title = "How to import street light from a csv file ?"
description = '''Hello, I&#x27;m help a little town in France who actually use Quantum Gis, i creat for us the database for 855 point of street light with other data like coordinate, power, lenght of the pole,... I can extract data to csv file but how can i import data directly to Openstreetmap ? I see on website i can p...'''
date = "2013-05-20T20:38:00Z"
lastmod = "2013-05-21T22:28:00Z"
weight = 22572
keywords = [ "import", "validate", "street", "light" ]
aliases = [ "/questions/22572" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [How to import street light from a csv file ?](/questions/22572/how-to-import-street-light-from-a-csv-file)

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
<span id="post-22572-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22572-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22572-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm help a little town in France who actually use Quantum Gis, i creat for us the database for 855 point of street light with other data like coordinate, power, lenght of the pole,...</p>
<p>I can extract data to csv file but how can i import data directly to Openstreetmap ?</p>
<p>I see on website i can put the data to Cartodb.com and display a layer above Openstreetmap, but it seem extremly complex for me.</p>
<p>I have no budget to create a GIS server.</p>
<p>Have you got a simple solution to do that ?</p>
<p>I wan't to tell to the mayor, the locals can participate in the update data. But how is defined the principle of validation is that the mayor has always given control over to revalidated. The goal is to be certain that erroneous data is not added.</p>
<p>Best regards.</p>
<p>Addition:</p>
<p>For readability I put only one line with the header, of course I can put following the OpenStreetMap format separation value as "," or ";" in the end you see the geographical coordinates Lambert93 I can convert WGS84 if necessary.</p>
<pre><code>REPERE  SECTEUR LIEU_DIT    CATEGORIE   TYPE_SUPPORT    ETAT    HAUTEUR_SUPPORT TYPE_LAMPE  NBRE_LAMPE  MARQUE  MODELE  DATE_POSE   ETAT    DERNIERE_INTERVENTION   COMMENTAIRE_1   COMMENTAIRE_2   PUISSANCE   Position X  Position Y
&#10;1   1   Avenue de Rodez Point lumineux  Candelabre  SATISFAISANT    8m  Lampe à sodium haute pression 100 watts 1   Thorn   Pilote  oct-98  SATISFAISANT                100 000000.00   0000000.00</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-validate" rel="tag" title="see questions tagged &#39;validate&#39;">validate</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-light" rel="tag" title="see questions tagged &#39;light&#39;">light</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 May '13, 20:38</strong></p>
<img src="https://secure.gravatar.com/avatar/cdf3989c29c421861b42d6d735d65bab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gabriel45895&#39;s gravatar image" />
<p><span>gabriel45895</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gabriel45895 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 May '13, 22:09</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-22572" class="comments-container">
<span id="22578"></span>
<div id="comment-22578" class="comment">
<div id="post-22578-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Aside from the technical question, make sure that you are aware that there are <a href="http://wiki.openstreetmap.org/wiki/Import/Guidelines">quality standards</a> for imports. In particular, consensus in the local community and documentation are mandatory. It's also good to have solid previous experience with OSM before performing an import.</p>
</div>
<div id="comment-22578-info" class="comment-info">
<span class="comment-age">(20 May '13, 21:48)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-22572" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22572-form-container" class="comment-form-container">
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

<span id="22583"></span>

<div id="answer-container-22583" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22583-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22583-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-22583-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please understand that in OSM there is no "protected" data. If you enter street lights into OSM then others can edit that data. You, the mayor, or others can watch these edits of course but you will not be asked to approve them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 May '13, 23:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-22583" class="comments-container">
&#10;</div>
<div id="comment-tools-22583" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22583-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="22589"></span>

<div id="answer-container-22589" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22589-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22589-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-22589-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a OpenData plugin (<a href="http://wiki.openstreetmap.org/wiki/JOSM/Plugins/OpenData)">http://wiki.openstreetmap.org/wiki/JOSM/Plugins/OpenData)</a> for the JOSM editor. It allows one to import CSV-files and can convert from a number of coordinate systems, such as Lambert. But as others wrote, the import of data has to be described on the wiki</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '13, 05:03</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-22589" class="comments-container">
<span id="22595"></span>
<div id="comment-22595" class="comment">
<div id="post-22595-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Because of this, I strongly recommend to coordinate with the french OSM community, who can be reached at <a href="http://forum.openstreetmap.org/viewforum.php?id=22">http://forum.openstreetmap.org/viewforum.php?id=22</a> .</p>
</div>
<div id="comment-22595-info" class="comment-info">
<span class="comment-age">(21 May '13, 10:32)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-22589" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22589-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="22573"></span>

<div id="answer-container-22573" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22573-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22573-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22573-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I usually convert csv to OSM format using awk, but you are maybe more happy with <a href="http://wiki.openstreetmap.org/wiki/User:Lübeck/csv2osm_local/source">this csv2osm script</a>.</p>
<p>hth<br />
malenki</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 May '13, 20:45</strong></p>
<img src="https://secure.gravatar.com/avatar/a18e2b8eb41515c09bb66159941584bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="malenki&#39;s gravatar image" />
<p><span>malenki</span><br />
<span class="score" title="4713 reputation points"><span>4.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="46 badges"><span class="silver">●</span><span class="badgecount">46</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="malenki has 10 accepted answers">6%</span> </br></p>
</div>
</div>
<div id="comments-container-22573" class="comments-container">
<span id="22576"></span>
<div id="comment-22576" class="comment">
<div id="post-22576-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you malenki for your fast answere.</p>
<p>I use windows and i don't know pearl language, i know GIS software like Quantum Gis, Autocad map 3D. I know xhtml, css and Autoit so you see i'm not really a programmer.</p>
<p>Can you develop me the whole process ?</p>
<p>1 - convert csv to OSM</p>
<p>2 - How to import 855 line in OSM into Openstreetmap ?</p>
<p>Thanks.</p>
</div>
<div id="comment-22576-info" class="comment-info">
<span class="comment-age">(20 May '13, 20:52)</span> <span class="comment-user userinfo">gabriel45895</span>
</div>
</div>
<span id="22612"></span>
<div id="comment-22612" class="comment">
<div id="post-22612-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The linked file contains helpful hints in English. As I said I didn't use it myself (it doesn't match my purposes). When you want to run it, you have to install the [perl environment][1] before. Then you can run the script with perl $scriptname.</p>
</div>
<div id="comment-22612-info" class="comment-info">
<span class="comment-age">(21 May '13, 22:28)</span> <span class="comment-user userinfo">malenki</span>
</div>
</div>
<span id="22613"></span>
<div id="comment-22613" class="comment">
<div id="post-22613-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>After converting you can load the OSM file with QGis or JOSM and check if the data is located and tagged correctly.</p>
<p>Before you upload anything you should have ticked off every point of the <a href="http://wiki.openstreetmap.org/wiki/FR:Import/Guidelines">Import Guidelines</a> - maybe compare if the English version of the guideline has some more information.</p>
<p>btw: I am less coder then you are. The little HTML I made I just copied. ;)</p>
</div>
<div id="comment-22613-info" class="comment-info">
<span class="comment-age">(21 May '13, 22:28)</span> <span class="comment-user userinfo">malenki</span>
</div>
</div>
</div>
<div id="comment-tools-22573" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22573-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="22575"></span>

<div id="answer-container-22575" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22575-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22575-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22575-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try adding csv in the blank window below Questions and youll find several similar questions and solutions. You even could transfer the inventarisation into a community project and add several participants to tag.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 May '13, 20:49</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 May '13, 20:54</strong> </span></p>
</div>
</div>
<div id="comments-container-22575" class="comments-container">
&#10;</div>
<div id="comment-tools-22575" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22575-form-container" class="comment-form-container">
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

