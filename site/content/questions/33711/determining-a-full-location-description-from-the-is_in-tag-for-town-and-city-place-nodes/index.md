+++
type = "question"
title = "Determining a full location description from the is_in tag for town and city place nodes"
description = '''Please note - sorry but I couldn&#x27;t get the question editor to show my XML so I&#x27;ve had to replace all the &#x27;&amp;lt;&#x27;s with &#x27;[&#x27; and all the &#x27;&amp;gt;&#x27;s with &#x27;]&#x27; in what follows. If someone knows how to fix this for me please let me know - thanks. I am building a simple application which, given a worldwide lat...'''
date = "2014-06-05T13:35:00Z"
lastmod = "2014-06-05T23:05:00Z"
weight = 33711
keywords = [ "mass_tagging", "reversegeocoding", "admin_boundary", "tagging", "is_in" ]
aliases = [ "/questions/33711" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Determining a full location description from the is_in tag for town and city place nodes](/questions/33711/determining-a-full-location-description-from-the-is_in-tag-for-town-and-city-place-nodes)

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
<span id="post-33711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33711-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><em>Please note - sorry but I couldn't get the question editor to show my XML so I've had to replace all the '&lt;'s with '[' and all the '&gt;'s with ']' in what follows. If someone knows how to fix this for me please let me know - thanks.</em></p>
<p>I am building a simple application which, given a worldwide lat/lon, requires details of the nearest city or town, based upon a simple as-the-crow-flies measurement. To achieve this I've chosen to use the OSM nodes which are tagged place='town' or place='city', calculating the spherical distance between my check point and each node's lat/lon. These nodes, according to <a href="https://wiki.openstreetmap.org/wiki/Key:place">https://wiki.openstreetmap.org/wiki/Key:place</a>, represent the approximate centre of each town and city and so are ideal for my requirement.</p>
<p>Given my chosen approach, I extracted the data from the Overpass API, using the following requests:</p>
<pre><code>curl http://www.overpass-api.de/api/xapi?node[place=city] -g -o worldcities.osm
curl http://www.overpass-api.de/api/xapi?node[place=town][@timeout=360] -g -o worldtowns.osm -g -o worldtowns.osm</code></pre>
<p>This has given me 2 files of data, which I'm loading (using osm2pgsql), giving me a database which is able to support my distance searching. Each database search will give me back a nearest town/city node, which I then need to display to my application user in text (not on a map), and so I need a location name/description. I want to show more than just the town/city name and so started looking at the is_in tag.</p>
<p>I'm seeing that some of the place nodes have is_in tags I can use directly, such as:</p>
<pre><code>[node id=&quot;271344&quot; lat=&quot;51.2569570&quot; lon=&quot;-1.6233744&quot;]
[tag k=&quot;is_in&quot; v=&quot;Wiltshire, England, UK&quot;/]
[tag k=&quot;name&quot; v=&quot;Ludgershall&quot;/]
[tag k=&quot;place&quot; v=&quot;town&quot;/]
[tag k=&quot;wikipedia&quot; v=&quot;en:Ludgershall, Wiltshire&quot;/]
[/node]</code></pre>
<p>I can use this to show 'Ludgershall, Wiltshire, England, UK' to my application user.</p>
<p>Others do not have an is_in tag:</p>
<pre><code>[node id=&quot;271099&quot; lat=&quot;50.9196406&quot; lon=&quot;-1.4894631&quot;]
[tag k=&quot;name&quot; v=&quot;Totton&quot;/]
[tag k=&quot;place&quot; v=&quot;town&quot;/]
[/node]</code></pre>
<p>Some have an is_in but also have 'component' is_in tags, which contain additional details:</p>
<pre><code>[node id=&quot;4085941&quot; lat=&quot;52.1363806&quot; lon=&quot;-0.4675041&quot;]
[tag k=&quot;is_in&quot; v=&quot;Bedfordshire&quot;/]
[tag k=&quot;is_in:country&quot; v=&quot;United Kingdom&quot;/]
[tag k=&quot;is_in:country_code&quot; v=&quot;GB&quot;/]
[tag k=&quot;is_in:county&quot; v=&quot;Bedfordshire&quot;/]
[tag k=&quot;name&quot; v=&quot;Bedford&quot;/]
[tag k=&quot;name:lt&quot; v=&quot;Bedfordas&quot;/]
[tag k=&quot;name:ru&quot; v=&quot;Ð‘ÐµÐ´Ñ„Ð¾Ñ€Ð´&quot;/]
[tag k=&quot;place&quot; v=&quot;town&quot;/]
[tag k=&quot;population&quot; v=&quot;80000&quot;/]
[tag k=&quot;wikipedia&quot; v=&quot;en:Bedford&quot;/]
[/node]</code></pre>
<p>Some only have components and no overall is_in to refer to:</p>
<pre><code>[node id=&quot;16664272&quot; lat=&quot;52.1365867&quot; lon=&quot;-0.9859244&quot;]
[tag k=&quot;is_in:continent&quot; v=&quot;Europe&quot;/]
[tag k=&quot;is_in:country&quot; v=&quot;United Kingdom&quot;/]
[tag k=&quot;is_in:country_code&quot; v=&quot;GB&quot;/]
[tag k=&quot;is_in:county&quot; v=&quot;Northamptonshire&quot;/]
[tag k=&quot;is_in:district&quot; v=&quot;South Northamptonshire&quot;/]
[tag k=&quot;name&quot; v=&quot;Towcester&quot;/]
[tag k=&quot;old_name&quot; v=&quot;Lactodurum&quot;/]
[tag k=&quot;place&quot; v=&quot;town&quot;/]
[tag k=&quot;wikipedia&quot; v=&quot;en:Towcester&quot;/]
[/node]</code></pre>
<p>Some are 'backwards' (it should be 'Surrey, England', not 'England, Surrey'):</p>
<pre><code>[node id=&quot;14698916&quot; lat=&quot;51.2321130&quot; lon=&quot;-0.3247823&quot;]
[tag k=&quot;is_in&quot; v=&quot;England, Surrey&quot;/]
[tag k=&quot;name&quot; v=&quot;Dorking&quot;/]
[tag k=&quot;place&quot; v=&quot;town&quot;/]
[tag k=&quot;wikipedia&quot; v=&quot;en:Dorking&quot;/]
[/node]</code></pre>
<p>Ideally I need a English name for each, but I'm seeing a mix of languages in some cases:</p>
<pre><code>[node id=&quot;18481614&quot; lat=&quot;51.8397184&quot; lon=&quot;6.6161534&quot;]
[tag k=&quot;is_in&quot; v=&quot;Kreis Borken,Regierungsbezirk Münster,Nordrhein-Westfalen,Bundesrepublik Deutschland,Europe&quot;/]
[tag k=&quot;is_in:continent&quot; v=&quot;Europe&quot;/]
[tag k=&quot;is_in:country&quot; v=&quot;Germany&quot;/]
[tag k=&quot;is_in:state&quot; v=&quot;North Rhine-Westphalia&quot;/]
[tag k=&quot;name&quot; v=&quot;Bocholt&quot;/]
[tag k=&quot;name:ru&quot; v=&quot;Бохольт&quot;/]
[tag k=&quot;place&quot; v=&quot;town&quot;/]
[tag k=&quot;population&quot; v=&quot;73696&quot;/]
[tag k=&quot;website&quot; v=&quot;http://www.bocholt.de&quot;/]
[tag k=&quot;wikipedia&quot; v=&quot;de:Bocholt&quot;/]
[/node]</code></pre>
<p>I've pretty much come to the conclusion that I can't depend on the data I'm seeing in the is_in tag as it currently stands, there is too much variation in the usage, so I've been working on an alternative solution.</p>
<p>I'm using the area queries which the Overpass API makes available, so given a town node such as:</p>
<pre><code>[node id=&quot;271099&quot; lat=&quot;50.9196406&quot; lon=&quot;-1.4894631&quot;]
[tag k=&quot;name&quot; v=&quot;Totton&quot;/]
[tag k=&quot;place&quot; v=&quot;town&quot;/]
[/node]</code></pre>
<p>I can make a query against the API using this request:</p>
<pre><code>http://overpass-api.de/api/interpreter?data=[out:json];is_in(50.9196406,-1.4894631);out;</code></pre>
<p>Which gives me... (sorry that this is quite long...):</p>
<pre><code>{
  &quot;version&quot;: 0.6,
  &quot;generator&quot;: &quot;Overpass API&quot;,
  &quot;osm3s&quot;: {
    &quot;timestamp_osm_base&quot;: &quot;2014-06-05T10:15:01Z&quot;,
    &quot;timestamp_areas_base&quot;: &quot;2014-06-05T01:00:02Z&quot;,
    &quot;copyright&quot;: &quot;The data included in this document is from www.openstreetmap.org. The data is made available under ODbL.&quot;
  },
  &quot;elements&quot;: [
&#10;{
  &quot;type&quot;: &quot;area&quot;,
  &quot;id&quot;: 2438387676,
  &quot;tags&quot;: {
    &quot;name&quot;: &quot;Southampton&quot;,
    &quot;public_transport&quot;: &quot;pay_scale_area&quot;,
    &quot;ref&quot;: &quot;SOTON&quot;,
    &quot;source&quot;: &quot;naptan_import&quot;
  }
}
,
{
  &quot;type&quot;: &quot;area&quot;,
  &quot;id&quot;: 3600058447,
  &quot;tags&quot;: {
    &quot;ISO3166-2&quot;: &quot;GB-ENG&quot;,
    &quot;admin_level&quot;: &quot;4&quot;,
    &quot;boundary&quot;: &quot;administrative&quot;,
    &quot;name&quot;: &quot;England&quot;,
    &quot;name:be&quot;: &quot;ÐÐ½Ð³Ð»Ñ–Ñ&quot;,
    &quot;name:cy&quot;: &quot;Lloegr&quot;,
    &quot;name:de&quot;: &quot;England&quot;,
    &quot;name:el&quot;: &quot;Î‘Î³Î³Î»Î¯Î±&quot;,
    &quot;name:en&quot;: &quot;England&quot;,
    &quot;name:es&quot;: &quot;Inglaterra&quot;,
    &quot;name:fr&quot;: &quot;Angleterre&quot;,
    &quot;name:gd&quot;: &quot;Sasainn&quot;,
    &quot;name:gv&quot;: &quot;Sostyn&quot;,
    &quot;name:hsb&quot;: &quot;JendÅºelska&quot;,
    &quot;name:hu&quot;: &quot;Anglia&quot;,
    &quot;name:it&quot;: &quot;Inghilterra&quot;,
    &quot;name:lt&quot;: &quot;Anglija&quot;,
    &quot;name:nl&quot;: &quot;Engeland&quot;,
    &quot;name:pl&quot;: &quot;Anglia&quot;,
    &quot;name:pt&quot;: &quot;Inglaterra&quot;,
    &quot;name:ru&quot;: &quot;ÐÐ½Ð³Ð»Ð¸Ñ&quot;,
    &quot;name:sv&quot;: &quot;England&quot;,
    &quot;name:uk&quot;: &quot;ÐÐ½Ð³Ð»Ñ–Ñ&quot;,
    &quot;name:vi&quot;: &quot;Anh&quot;,
    &quot;name:zh&quot;: &quot;è‹±æ ¼è˜­&quot;,
    &quot;name:zh-classical&quot;: &quot;è‹±æ ¼è˜­&quot;,
    &quot;name:zh-simplified&quot;: &quot;è‹±æ ¼å…°&quot;,
    &quot;name:zh-traditional&quot;: &quot;è‹±æ ¼è˜­&quot;,
    &quot;old_name:vi&quot;: &quot;Anh Quá»‘c&quot;,
    &quot;type&quot;: &quot;boundary&quot;,
    &quot;wikidata&quot;: &quot;Q21&quot;,
    &quot;wikipedia&quot;: &quot;en:England&quot;
  }
}
,
{
  &quot;type&quot;: &quot;area&quot;,
  &quot;id&quot;: 3600062149,
  &quot;tags&quot;: {
    &quot;ISO3166-1&quot;: &quot;GB&quot;,
    &quot;ISO3166-1:alpha2&quot;: &quot;GB&quot;,
    &quot;ISO3166-1:alpha3&quot;: &quot;GBR&quot;,
    &quot;ISO3166-1:numeric&quot;: &quot;826&quot;,
    &quot;admin_level&quot;: &quot;2&quot;,
    &quot;boundary&quot;: &quot;administrative&quot;,
    &quot;currency&quot;: &quot;GBP&quot;,
    &quot;driving_side&quot;: &quot;left&quot;,
    &quot;flag&quot;: &quot;http://upload.wikimedia.org/wikipedia/commons/a/ae/Flag_of_the_United_Kingdom.svg&quot;,
    &quot;int_name&quot;: &quot;United Kingdom&quot;,
    &quot;name&quot;: &quot;United Kingdom&quot;,
    &quot;name:ab&quot;: &quot;Ð‘Ñ€Ð¸Ñ‚Ð°Ð½Ð¸Ð° Ð”Ñƒ&quot;,
    &quot;name:af&quot;: &quot;Verenigde Koninkryk&quot;,
    &quot;name:ak&quot;: &quot;United Kingdom&quot;,
    &quot;name:als&quot;: &quot;Vereinigtes KÃ¶nigreich&quot;,
    &quot;name:am&quot;: &quot;á‹©áŠ“á‹­á‰µá‹µ áŠªáŠ•áŒá‹°áˆ&quot;,
    &quot;name:an&quot;: &quot;Reino Unito&quot;,
    &quot;name:ang&quot;: &quot;GeÄned CynerÄ«ce&quot;,
    &quot;name:ar&quot;: &quot;Ø§Ù„Ù…Ù…Ù„ÙƒØ© Ø§Ù„Ù…ØªØ­Ø¯Ø©&quot;,
    &quot;name:arc&quot;: &quot;Ü¡Ü ÜŸÜ˜Ü¬Ü Ü¡ÜšÜÜ•Ü¬Ü&quot;,
    &quot;name:arz&quot;: &quot;Ø§Ù„Ù…Ù…Ù„ÙƒÙ‡ Ø§Ù„Ù…ØªØ­Ø¯Ù‡&quot;,
    &quot;name:ast&quot;: &quot;Reinu XunÃ­u&quot;,
    &quot;name:az&quot;: &quot;BÃ¶yÃ¼k Britaniya&quot;,
    &quot;name:ba&quot;: &quot;Ð‘Ó©Ð¹Ó©Ðº Ð‘Ñ€Ð¸Ñ‚Ð°Ð½Ð¸Ñ&quot;,
    &quot;name:bar&quot;: &quot;Vaeinigts Kinireich&quot;,
    &quot;name:bat-smg&quot;: &quot;JongtÄ—nÄ— KaralÄ«stÄ—&quot;,
    &quot;name:bcl&quot;: &quot;Reyno Unido&quot;,
    &quot;name:be&quot;: &quot;Ð’ÑÐ»Ñ–ÐºÐ°Ð±Ñ€Ñ‹Ñ‚Ð°Ð½Ñ–Ñ&quot;,
    &quot;name:be-x-old&quot;: &quot;Ð’ÑÐ»Ñ–ÐºÐ°Ð±Ñ€Ñ‹Ñ‚Ð°Ð½Ñ–Ñ&quot;,
    &quot;name:bg&quot;: &quot;ÐžÐ±ÐµÐ´Ð¸Ð½ÐµÐ½Ð¾ ÐºÑ€Ð°Ð»ÑÑ‚Ð²Ð¾ Ð’ÐµÐ»Ð¸ÐºÐ¾Ð±Ñ€Ð¸Ñ‚Ð°Ð½Ð¸Ñ Ð¸ Ð¡ÐµÐ²ÐµÑ€Ð½Ð° Ð˜Ñ€Ð»Ð°Ð½Ð´Ð¸Ñ&quot;,
    &quot;name:bi&quot;: &quot;Unaeted Kingdom&quot;,
    &quot;name:bjn&quot;: &quot;Britania Raya&quot;,
    &quot;name:bn&quot;: &quot;à¦¯à§à¦•à§à¦¤à¦°à¦¾à¦œà§à¦¯&quot;,
    &quot;name:bo&quot;: &quot;à½‘à½–à¾±à½²à½“à¼‹à½‡à½²à¼‹à½˜à½‰à½˜à¼‹à½ à½–à¾²à½ºà½£à¼&quot;,
    &quot;name:bpy&quot;: &quot;à¦¤à¦¿à¦²à¦ªà¦¾à¦°à¦¾à¦œà§à¦¯&quot;,
    &quot;name:br&quot;: &quot;Rouantelezh-Unanet&quot;,
    &quot;name:bs&quot;: &quot;Ujedinjeno Kraljevstvo Velike Britanije i Sjeverne Irske&quot;,
    &quot;name:bug&quot;: &quot;United Kingdom&quot;,
    &quot;name:bxr&quot;: &quot;ÐÑÐ³Ð´ÑÑÐ½ Ð’Ð°Ð½Ñ‚ Ð£Ð»Ñ&quot;,
    &quot;name:ca&quot;: &quot;Regne Unit&quot;,
    &quot;name:cbk-zam&quot;: &quot;Reinos Unidos de Gran Britania y Norte Irelandia&quot;,
    &quot;name:cdo&quot;: &quot;Ä¬ng-guÃ³k&quot;,
    &quot;name:ce&quot;: &quot;Ð™Ð¾ÐºÐºÑ…Ð° Ð‘Ñ€Ð¸Ñ‚Ð°Ð½Ð¸&quot;,
    &quot;name:ceb&quot;: &quot;Hiniusang Gingharian&quot;,
    &quot;name:chr&quot;: &quot;áŽ¡áŽµááŽ¯&quot;,
    &quot;name:chy&quot;: &quot;United Kingdom&quot;,
    &quot;name:ckb&quot;: &quot;Ø´Ø§Ù†Ø´ÛŒÙ†ÛŒ ÛŒÛ•Ú©Ú¯Ø±ØªÙˆÙˆ&quot;,
    &quot;name:co&quot;: &quot;Regnu Unitu&quot;,
    &quot;name:crh&quot;: &quot;BÃ¼yÃ¼k Britaniya&quot;,
    &quot;name:cs&quot;: &quot;SpojenÃ© krÃ¡lovstvÃ­&quot;,
    &quot;name:csb&quot;: &quot;WiÃ´lgÃ´ BritanijÃ´&quot;,
    &quot;name:cu&quot;: &quot;Ð’Ñ”Ð»Ð¸ÐºÐ° Ð‘Ñ€Ð¸Ñ‚Ð°Ð½Ñ—ê™—&quot;,
    &quot;name:cv&quot;: &quot;ÐÑÐ»Äƒ Ð‘Ñ€Ð¸Ñ‚Ð°Ð½Ð¸&quot;,
    &quot;name:cy&quot;: &quot;Deyrnas Unedig&quot;,
    &quot;name:da&quot;: &quot;Storbritannien&quot;,
    &quot;name:de&quot;: &quot;Vereinigtes KÃ¶nigreich GroÃŸbritannien und Nordirland&quot;,
    &quot;name:diq&quot;: &quot;Qraliya Yewbiyayiye&quot;,
    &quot;name:dsb&quot;: &quot;Wjelika Britaniska&quot;,
    &quot;name:dv&quot;: &quot;Þ”ÞªÞ‚Þ¦Þ‡Þ¨Þ“Þ¬Þ‘Þ° Þ†Þ¨Þ‚Þ°ÞŽÞ°Þ‘Þ¦Þ‰Þ°&quot;,
    &quot;name:dz&quot;: &quot;à½¡à½´à¼‹à½“à½ à½²à¼‹à½Šà½ºà½Šà¼‹à½€à½²à½„à¼‹à½Œà½˜&quot;,
    &quot;name:ee&quot;: &quot;United Kingdom&quot;,
    &quot;name:el&quot;: &quot;Î—Î½Ï‰Î¼Î­Î½Î¿ Î’Î±ÏƒÎ¯Î»ÎµÎ¹Î¿&quot;,
    &quot;name:eml&quot;: &quot;RÃ©gn UnÃ®&quot;,
    &quot;name:en&quot;: &quot;United Kingdom&quot;,
    &quot;name:eo&quot;: &quot;UnuiÄinta ReÄlando&quot;,
    &quot;name:es&quot;: &quot;Reino Unido&quot;,
    &quot;name:et&quot;: &quot;Suurbritannia&quot;,
    &quot;name:eu&quot;: &quot;Erresuma Batua&quot;,
    &quot;name:ext&quot;: &quot;RÃ©inu Uniu&quot;,
    &quot;name:fa&quot;: &quot;Ø¨Ø±ÛŒØªØ§Ù†ÛŒØ§&quot;,
    &quot;name:fi&quot;: &quot;Yhdistynyt kuningaskunta&quot;,
    &quot;name:fiu-vro&quot;: &quot;Ãœtiskuningriik&quot;,
    &quot;name:fo&quot;: &quot;StÃ³ra Bretland&quot;,
    &quot;name:fr&quot;: &quot;Royaume-Uni&quot;,
    &quot;name:frp&quot;: &quot;RoyÃ´mo-Uni&quot;,
    &quot;name:frr&quot;: &quot;Feriind Kiningrik&quot;,
    &quot;name:fur&quot;: &quot;Ream UnÃ®t&quot;,
    &quot;name:fy&quot;: &quot;Grut-Brittanje&quot;,
    &quot;name:ga&quot;: &quot;An RÃ­ocht Aontaithe&quot;,
    &quot;name:gag&quot;: &quot;BÃ¼Ã¼k Britaniya&quot;,
    &quot;name:gan&quot;: &quot;è‹±åœ‹&quot;,
    &quot;name:gd&quot;: &quot;An RÃ¬oghachd Aonaichte&quot;,
    &quot;name:gl&quot;: &quot;Reino Unido&quot;,
    &quot;name:gn&quot;: &quot;TavetÃ£ Joaju&quot;,
    &quot;name:gu&quot;: &quot;àª¯à«àª¨àª¾àª‡àªŸà«‡àª¡ àª•àª¿àª‚àª—àª¡àª®&quot;,
    &quot;name:gv&quot;: &quot;Reeriaght Unnaneysit&quot;,
    &quot;name:ha&quot;: &quot;Birtaniya&quot;,
    &quot;name:hak&quot;: &quot;YÃ®n-koet&quot;,
    &quot;name:haw&quot;: &quot;Aupuni MÅÊ»Ä« Hui PÅ« Ê»ia&quot;,
    &quot;name:he&quot;: &quot;×”×ž×ž×œ×›×” ×”×ž××•×—×“×ª&quot;,
    &quot;name:hi&quot;: &quot;à¤¯à¥‚à¤¨à¤¾à¤‡à¤Ÿà¥‡à¤¡ à¤•à¤¿à¤‚à¤—à¤¡à¤®&quot;,
    &quot;name:hif&quot;: &quot;United Kingdom&quot;,
    &quot;name:hr&quot;: &quot;Ujedinjeno Kraljevstvo Velike Britanije i Sjeverne Irske&quot;,
    &quot;name:hsb&quot;: &quot;ZjednoÄ‡ene kralestwo&quot;,
    &quot;name:ht&quot;: &quot;WayÃ²m Ini&quot;,
    &quot;name:hu&quot;: &quot;EgyesÃ¼lt KirÃ¡lysÃ¡g&quot;,
    &quot;name:hy&quot;: &quot;Õ„Õ«Õ¡ÖÕµÕ¡Õ¬ Ô¹Õ¡Õ£Õ¡Õ¾Õ¸Ö€Õ¸Ö‚Õ©ÕµÕ¸Ö‚Õ¶&quot;,
    &quot;name:ia&quot;: &quot;Regno Unite&quot;,
    &quot;name:id&quot;: &quot;Britania Raya&quot;,
    &quot;name:ie&quot;: &quot;Reyatu Unit&quot;,
    &quot;name:ig&quot;: &quot;ObodoÃ©zÃ¨ NÃ  OfÃº&quot;,
    &quot;name:ilo&quot;: &quot;Nagkaykaysa a Pagarian&quot;,
    &quot;name:io&quot;: &quot;Unionita Rejio&quot;,
    &quot;name:is&quot;: &quot;Bretland&quot;,
    &quot;name:it&quot;: &quot;Regno Unito&quot;,
    &quot;name:ja&quot;: &quot;ã‚¤ã‚®ãƒªã‚¹&quot;,
    &quot;name:jbo&quot;: &quot;gugdegubu&quot;,
    &quot;name:jv&quot;: &quot;Britania Raya&quot;,
    &quot;name:ka&quot;: &quot;áƒ’áƒáƒ”áƒ áƒ—áƒ˜áƒáƒœáƒ”áƒ‘áƒ£áƒšáƒ˜ áƒ¡áƒáƒ›áƒ”áƒ¤áƒ&quot;,
    &quot;name:kab&quot;: &quot;Legliz&quot;,
    &quot;name:kbd&quot;: &quot;Ð‘Ñ€Ð¸Ñ‚Ð°Ð½Ð¸ÑÑˆÑ…ÑƒÑ&quot;,
    &quot;name:kg&quot;: &quot;Royaume-Uni&quot;,
    &quot;name:kk&quot;: &quot;Ò°Ð»Ñ‹Ð±Ñ€Ð¸Ñ‚Ð°Ð½Ð¸Ñ&quot;,
    &quot;name:kl&quot;: &quot;Tuluit Nunaat&quot;,
    &quot;name:km&quot;: &quot;ážšáž¶áž‡áž¶ážŽáž¶áž…áž€áŸ’ážšážšáž½áž˜&quot;,
    &quot;name:kn&quot;: &quot;à²¯à³à²¨à³ˆà²Ÿà³†à²¡à³ à²•à²¿à²‚à²—à³â€Œà²¡à²‚&quot;,
    &quot;name:ko&quot;: &quot;ì˜êµ­&quot;,
    &quot;name:koi&quot;: &quot;Ð«Ð´Ð¶Ñ‹Ñ‚ Ð‘Ñ€Ð¸Ñ‚Ð¼Ñƒ&quot;,
    &quot;name:krc&quot;: &quot;Ð£Ð»Ð»Ñƒ Ð‘Ñ€Ð¸Ñ‚Ð°Ð½Ð¸Ñ&quot;,
    &quot;name:ksh&quot;: &quot;JruÃŸbritannie&quot;,
    &quot;name:ku&quot;: &quot;Keyaniya YekbÃ»yÃ®&quot;,
    &quot;name:kv&quot;: &quot;Ð«Ð´Ð¶Ñ‹Ð´ Ð‘Ñ€Ð¸Ñ‚Ð°Ð½Ð¸Ñ&quot;,
    &quot;name:kw&quot;: &quot;Ruwvaneth Unys&quot;,
    &quot;name:ky&quot;: &quot;Ð£Ð»ÑƒÑƒ Ð‘Ñ€Ð¸Ñ‚Ð°Ð½Ð¸Ñ Ð¶Ð°Ð½Ð° Ð¢Ò¯Ð½Ð´Ò¯Ðº Ð˜Ñ€Ð»Ð°Ð½Ð´Ð¸Ñ&quot;,
    &quot;name:la&quot;: &quot;Britanniarum Regnum&quot;,
    &quot;name:lad&quot;: &quot;Reyno Unido&quot;,
    &quot;name:lb&quot;: &quot;Groussbritannien an Nordirland&quot;,
    &quot;name:lez&quot;: &quot;Ð§IÐµÑ…Ð¸Ð±Ñ€Ð¸Ñ‚Ð°Ð½Ð¸Ñ&quot;,
    &quot;name:li&quot;: &quot;Vereineg Keuninkriek&quot;,
    &quot;name:lij&quot;: &quot;Regno UnÃ¯o&quot;,
    &quot;name:lmo&quot;: &quot;Regn ÃœnÃ¬&quot;,
    &quot;name:ln&quot;: &quot;IngÉ›lÉ›ÌtÉ›lÉ›&quot;,
    &quot;name:lt&quot;: &quot;JungtinÄ— KaralystÄ—&quot;,
    &quot;name:ltg&quot;: &quot;Lelbrytaneja&quot;,
    &quot;name:lv&quot;: &quot;ApvienotÄ Karaliste&quot;,
    &quot;name:mg&quot;: &quot;Fanjakana Mitambatra&quot;,
    &quot;name:mhr&quot;: &quot;Ð£ÑˆÑ‹Ð¼Ð¾ ÐšÐ¾Ñ€Ð¾Ð»ÐµÐ²ÑÑ‚Ð²Ðµ&quot;,
    &quot;name:mi&quot;: &quot;KÄ«ngitanga Kotahi&quot;,
    &quot;name:mk&quot;: &quot;ÐžÐ±ÐµÐ´Ð¸Ð½ÐµÑ‚Ð¾ ÐšÑ€Ð°Ð»ÑÑ‚Ð²Ð¾&quot;,
    &quot;name:ml&quot;: &quot;à´¯àµà´£àµˆà´±àµà´±à´¡àµ à´•à´¿à´™àµà´¡à´‚&quot;,
    &quot;name:mn&quot;: &quot;Ð˜Ñ… Ð‘Ñ€Ð¸Ñ‚Ð°Ð½Ð¸&quot;,
    &quot;name:mr&quot;: &quot;à¤¯à¥à¤¨à¤¾à¤¯à¤Ÿà¥‡à¤¡ à¤•à¤¿à¤‚à¤—à¥à¤¡à¤®&quot;,
    &quot;name:mrj&quot;: &quot;ÐšÐ¾Ð³Ð¾ Ð‘Ñ€Ð¸Ñ‚Ð°Ð½Ð¸&quot;,
    &quot;name:ms&quot;: &quot;United Kingdom&quot;,
    &quot;name:mt&quot;: &quot;Renju Unit&quot;,
    &quot;name:mwl&quot;: &quot;Reino Ounido&quot;,
    &quot;name:my&quot;: &quot;á€šá€°á€”á€­á€¯á€€á€ºá€á€€á€ºá€€á€„á€ºá€¸á€’á€™á€ºá€¸á€”á€­á€¯á€„á€ºá€„á€¶&quot;,
    &quot;name:mzn&quot;: &quot;Ø¨Ø±ÛŒØªØ§Ù†ÛŒØ§&quot;,
    &quot;name:na&quot;: &quot;Ingerand&quot;,
    &quot;name:nah&quot;: &quot;TlacetilÄ«lli HuÄ“yitlahtohcÄyÅtl&quot;,
    &quot;name:nap&quot;: &quot;Gran Vretagna&quot;,
    &quot;name:nds&quot;: &quot;Vereenigt KÃ¶nigriek vun Grootbritannien un Noordirland&quot;,
    &quot;name:nds-nl&quot;: &quot;Verienigd Keuninkriek&quot;,
    &quot;name:ne&quot;: &quot;à¤¸à¤‚à¤¯à¥à¤•à¥à¤¤ à¤…à¤§à¤¿à¤°à¤¾à¤œà¥à¤¯&quot;,
    &quot;name:nl&quot;: &quot;Verenigd Koninkrijk&quot;,
    &quot;name:nn&quot;: &quot;Storbritannia&quot;,
    &quot;name:no&quot;: &quot;Storbritannia&quot;,
    &quot;name:nov&quot;: &quot;Unionati Regia&quot;,
    &quot;name:nrm&quot;: &quot;Rouoyaume Unni&quot;,
    &quot;name:nv&quot;: &quot;TÃ³taÊ¼ DinÃ©Ê¼iÊ¼ BikÃ©yah&quot;,
    &quot;name:oc&quot;: &quot;Reialme Unit&quot;,
    &quot;name:or&quot;: &quot;à¬¯à­à¬•à­à¬¤à¬°à¬¾à¬œà­à­Ÿ&quot;,
    &quot;name:os&quot;: &quot;Ð¡Ñ‚Ñ‹Ñ€ Ð‘Ñ€Ð¸Ñ‚Ð°Ð½Ð¸&quot;,
    &quot;name:pa&quot;: &quot;à¨¸à©°à¨¯à©à¨•à¨¤ à¨¬à¨¾à¨¦à¨¸à¨¼à¨¾à¨¹à©€&quot;,
    &quot;name:pag&quot;: &quot;Reino Unido&quot;,
    &quot;name:pam&quot;: &quot;Pisanmetung a Ka-arian&quot;,
    &quot;name:pap&quot;: &quot;Reino Uni&quot;,
    &quot;name:pcd&quot;: &quot;RoÃ©yÃ´me-Uni&quot;,
    &quot;name:pih&quot;: &quot;Yunitid Kingdum&quot;,
    &quot;name:pl&quot;: &quot;Wielka Brytania&quot;,
    &quot;name:pms&quot;: &quot;Regn UnÃ¬&quot;,
    &quot;name:pnb&quot;: &quot;Ø¨Ø±Ø·Ø§Ù†ÛŒÛ&quot;,
    &quot;name:pnt&quot;: &quot;Î—Î½Ï‰Î¼Î­Î½Î¿ Î’Î±ÏƒÎ¯Î»ÎµÎ¹Î¿&quot;,
    &quot;name:ps&quot;: &quot;Ø¨Ø±ÙŠØªØ§Ù†ÙŠØ§&quot;,
    &quot;name:pt&quot;: &quot;Reino Unido&quot;,
    &quot;name:qu&quot;: &quot;Hukllachasqa Qhapaq Suyu&quot;,
    &quot;name:rm&quot;: &quot;Reginavel UnÃ¬&quot;,
    &quot;name:rmy&quot;: &quot;Phandlo Thagaripen la Bare Britaniyako thai le Nordutne Irlandesko&quot;,
    &quot;name:ro&quot;: &quot;Regatul Unit al Marii Britanii È™i al Irlandei de Nord&quot;,
    &quot;name:roa-rup&quot;: &quot;Britania Mari&quot;,
    &quot;name:roa-tara&quot;: &quot;Regne AunÃ¬te&quot;,
    &quot;name:ru&quot;: &quot;Ð’ÐµÐ»Ð¸ÐºÐ¾Ð±Ñ€Ð¸Ñ‚Ð°Ð½Ð¸Ñ&quot;,
    &quot;name:rue&quot;: &quot;Ð’ÐµÐ»Ð¸ÐºÐ° Ð‘Ñ€Ñ–Ñ‚Ð°Ð½Ñ–Ñ&quot;,
    &quot;name:rw&quot;: &quot;Ubwongereza&quot;,
    &quot;name:sa&quot;: &quot;à¤¸à¤‚à¤¯à¥à¤•à¥à¤¤ à¤…à¤§à¤¿à¤°à¤¾à¤œà¥à¤¯&quot;,
    &quot;name:sah&quot;: &quot;Ð¥Ð¾Ð»Ð±Ð¾hÑƒÐºÑ‚Ð°Ð°Ñ… Ð¥Ð¾Ñ€ÑƒÐ¾Ð»Ð»ÑƒÐº&quot;,
    &quot;name:sc&quot;: &quot;Rennu Auniadu&quot;,
    &quot;name:scn&quot;: &quot;Regnu Unitu&quot;,
    &quot;name:sco&quot;: &quot;Unitit Kinrick&quot;,
    &quot;name:se&quot;: &quot;Ovttastuvvan gonagasriika&quot;,
    &quot;name:sh&quot;: &quot;Ujedinjeno Kraljevstvo&quot;,
    &quot;name:si&quot;: &quot;à¶‘à¶šà·Šà·ƒà¶­à·Š à¶»à·à¶¢à¶°à·à¶±à·’à¶º&quot;,
    &quot;name:simple&quot;: &quot;United Kingdom&quot;,
    &quot;name:sk&quot;: &quot;SpojenÃ© krÃ¡Ä¾ovstvo&quot;,
    &quot;name:sl&quot;: &quot;ZdruÅ¾eno kraljestvo Velike Britanije in Severne Irske&quot;,
    &quot;name:sn&quot;: &quot;United Kingdom&quot;,
    &quot;name:so&quot;: &quot;Midowga boqortooyada Britan&quot;,
    &quot;name:sq&quot;: &quot;MbretÃ«ria e Bashkuar e BritanisÃ« dhe IrlandÃ«s sÃ« Veriut&quot;,
    &quot;name:sr&quot;: &quot;Ð£Ñ˜ÐµÐ´Ð¸ÑšÐµÐ½Ð¾ ÐšÑ€Ð°Ñ™ÐµÐ²ÑÑ‚Ð²Ð¾&quot;,
    &quot;name:srn&quot;: &quot;Ingriskondre&quot;,
    &quot;name:ss&quot;: &quot;United Kingdom&quot;,
    &quot;name:stq&quot;: &quot;Fereeniged KÃ¶Ã¶nichriek fon Groot-Britannien un Noudirlound&quot;,
    &quot;name:su&quot;: &quot;Britania&quot;,
    &quot;name:sv&quot;: &quot;Storbritannien&quot;,
    &quot;name:sw&quot;: &quot;Ufalme wa Muungano&quot;,
    &quot;name:szl&quot;: &quot;Wjelgo BrytaÅ„ijo&quot;,
    &quot;name:ta&quot;: &quot;à®à®•à¯à®•à®¿à®¯ à®‡à®°à®¾à®šà¯à®šà®¿à®¯à®®à¯&quot;,
    &quot;name:te&quot;: &quot;à°¯à±à°¨à±ˆà°Ÿà±†à°¡à± à°•à°¿à°‚à°—à±â€Œà°¡à°®à±&quot;,
    &quot;name:tet&quot;: &quot;Reinu Naklibur&quot;,
    &quot;name:tg&quot;: &quot;ÐŸÐ¾Ð´ÑˆÐ¾Ò³Ð¸Ð¸ ÐœÑƒÑ‚Ñ‚Ð°Ò³Ð¸Ð´Ð°&quot;,
    &quot;name:th&quot;: &quot;à¸ªà¸«à¸£à¸²à¸Šà¸­à¸²à¸“à¸²à¸ˆà¸±à¸à¸£&quot;,
    &quot;name:tl&quot;: &quot;Nagkakaisang Kaharian&quot;,
    &quot;name:tpi&quot;: &quot;Yunaitet Kingdom&quot;,
    &quot;name:tr&quot;: &quot;BirleÅŸik KrallÄ±k&quot;,
    &quot;name:tt&quot;: &quot;Ð‘Ó©ÐµÐºÐ±Ñ€Ð¸Ñ‚Ð°Ð½Ð¸Ñ&quot;,
    &quot;name:tw&quot;: &quot;United Kingdom&quot;,
    &quot;name:ty&quot;: &quot;ParatÄne&quot;,
    &quot;name:udm&quot;: &quot;Ð’ÐµÐ»Ð¸ÐºÐ¾Ð±Ñ€Ð¸Ñ‚Ð°Ð½Ð¸Ñ&quot;,
    &quot;name:ug&quot;: &quot;Ø¨ÛˆÙŠÛˆÙƒ Ø¨ÛØ±Ù‰ØªØ§Ù†Ù‰ÙŠÛ•&quot;,
    &quot;name:uk&quot;: &quot;Ð’ÐµÐ»Ð¸ÐºÐ° Ð‘Ñ€Ð¸Ñ‚Ð°Ð½Ñ–Ñ&quot;,
    &quot;name:ur&quot;: &quot;Ø¨Ø±Ø·Ø§Ù†ÛŒÛ&quot;,
    &quot;name:uz&quot;: &quot;Birlashgan Qirollik&quot;,
    &quot;name:vec&quot;: &quot;Regno UnÃ¬o&quot;,
    &quot;name:vep&quot;: &quot;Sur&#39; Britanii&quot;,
    &quot;name:vi&quot;: &quot;VÆ°Æ¡ng quá»‘c Anh&quot;,
    &quot;name:vls&quot;: &quot;VerÃªnigd Keunienkryk&quot;,
    &quot;name:vo&quot;: &quot;RegÃ¤n PebalÃ¶l&quot;,
    &quot;name:war&quot;: &quot;Reino Unido&quot;,
    &quot;name:wo&quot;: &quot;Nguur-Yu-Bennoo&quot;,
    &quot;name:wuu&quot;: &quot;è‹±å›½&quot;,
    &quot;name:xal&quot;: &quot;Ð˜Ðº Ð‘Ñ€Ð¸Ñ‚Ð¸ÑˆÐ¸Ð½ Ð±Ð¾Ð»Ð½ ÐÑ€ Ð“Ó™Ó™Ð»Ð³Ò¯Ð´Ð¸Ð½ ÐÐ¸Ð¸Ñ†Ó™Ñ‚Ó™ ÐÑƒÑ‚Ð³&quot;,
    &quot;name:xmf&quot;: &quot;áƒ’áƒáƒáƒ áƒ—áƒáƒ˜áƒáƒœáƒáƒ¤áƒ˜áƒšáƒ˜ áƒáƒ›áƒáƒ¤áƒ”&quot;,
    &quot;name:yi&quot;: &quot;×¤××¨××™×™× ×™×’×˜×¢ ×§×¢× ×™×’×¨×™×™×š&quot;,
    &quot;name:yo&quot;: &quot;Iláº¹Ì€á»ba Aá¹£á»Ì€kan&quot;,
    &quot;name:za&quot;: &quot;Yinghgoz&quot;,
    &quot;name:zea&quot;: &quot;VereÃªnigd Konienkriek&quot;,
    &quot;name:zh&quot;: &quot;è‹±å›½&quot;,
    &quot;name:zh-classical&quot;: &quot;è‹±åœ‹&quot;,
    &quot;name:zh-min-nan&quot;: &quot;LiÃ¢n-haÌp Ã”ng-kok&quot;,
    &quot;name:zh-simplified&quot;: &quot;è‹±å›½&quot;,
    &quot;name:zh-traditional&quot;: &quot;è‹±åœ‹&quot;,
    &quot;name:zh-yue&quot;: &quot;è‹±åœ‹&quot;,
    &quot;name:zu&quot;: &quot;Umbuso Ohlangeneyo&quot;,
    &quot;native_name&quot;: &quot;United Kingdom of Great Britain and Northern Ireland&quot;,
    &quot;native_name:da&quot;: &quot;Det Forenede Kongerige Storbritannien og Nordirland&quot;,
    &quot;native_name:es&quot;: &quot;Reino Unido de Gran BretaÃ±a e Irlanda del Norte&quot;,
    &quot;native_name:vi&quot;: &quot;VÆ°Æ¡ng quá»‘c LiÃªn hiá»‡p Anh vÃ  Báº¯c Ireland&quot;,
    &quot;official_name:en&quot;: &quot;United Kingdom of Great Britain and Northern Ireland&quot;,
    &quot;official_name:it&quot;: &quot;Regno Unito di Gran Bretagna e Irlanda del Nord&quot;,
    &quot;timezone&quot;: &quot;Europe/London&quot;,
    &quot;type&quot;: &quot;boundary&quot;,
    &quot;wikidata&quot;: &quot;Q145&quot;,
    &quot;wikipedia&quot;: &quot;en:United Kingdom&quot;
  }
}
,
{
  &quot;type&quot;: &quot;area&quot;,
  &quot;id&quot;: 3600129306,
  &quot;tags&quot;: {
    &quot;admin_level&quot;: &quot;8&quot;,
    &quot;boundary&quot;: &quot;administrative&quot;,
    &quot;designation&quot;: &quot;non_metropolitan_district&quot;,
    &quot;name&quot;: &quot;New Forest&quot;,
    &quot;population&quot;: &quot;174309&quot;,
    &quot;ref:gss&quot;: &quot;E07000091&quot;,
    &quot;ref:lau:1&quot;: &quot;UKJ3308&quot;,
    &quot;source:ref:gss&quot;: &quot;OS_OpenData_Boundary-Line&quot;,
    &quot;source:ref:lau&quot;: &quot;ONS_OpenData&quot;,
    &quot;type&quot;: &quot;boundary&quot;,
    &quot;website&quot;: &quot;http://www.newforest.gov.uk/&quot;,
    &quot;wikipedia&quot;: &quot;en:New Forest District&quot;
  }
}
,
{
  &quot;type&quot;: &quot;area&quot;,
  &quot;id&quot;: 3600151304,
  &quot;tags&quot;: {
    &quot;admin_level&quot;: &quot;5&quot;,
    &quot;boundary&quot;: &quot;administrative&quot;,
    &quot;name&quot;: &quot;South East England&quot;,
    &quot;name:de&quot;: &quot;SÃ¼dostengland&quot;,
    &quot;name:en&quot;: &quot;South East England&quot;,
    &quot;ref:gss&quot;: &quot;E12000008&quot;,
    &quot;ref:nuts:1&quot;: &quot;UKJ&quot;,
    &quot;source:ref:gss&quot;: &quot;ONS_OpenData&quot;,
    &quot;type&quot;: &quot;boundary&quot;,
    &quot;wikipedia&quot;: &quot;en:South East England&quot;
  }
}
,
{
  &quot;type&quot;: &quot;area&quot;,
  &quot;id&quot;: 3600172799,
  &quot;tags&quot;: {
    &quot;admin_level&quot;: &quot;6&quot;,
    &quot;boundary&quot;: &quot;administrative&quot;,
    &quot;designation&quot;: &quot;non_metropolitan_county&quot;,
    &quot;name&quot;: &quot;Hampshire&quot;,
    &quot;note&quot;: &quot;Inner ring is to seperate Hampshire from Southampton which is a UA&quot;,
    &quot;population&quot;: &quot;1304844&quot;,
    &quot;ref:gss&quot;: &quot;E10000014&quot;,
    &quot;ref:nuts:3&quot;: &quot;UKJ33&quot;,
    &quot;source:ref:gss&quot;: &quot;OS_OpenData_Boundary-Line&quot;,
    &quot;source:ref:nuts&quot;: &quot;ONS_OpenData&quot;,
    &quot;type&quot;: &quot;boundary&quot;,
    &quot;website&quot;: &quot;http://www.hampshire.gov.uk/&quot;,
    &quot;wikipedia&quot;: &quot;en:Hampshire&quot;
  }
}
,
{
  &quot;type&quot;: &quot;area&quot;,
  &quot;id&quot;: 3602698314,
  &quot;tags&quot;: {
    &quot;boundary&quot;: &quot;ceremonial&quot;,
    &quot;name&quot;: &quot;Hampshire&quot;,
    &quot;note&quot;: &quot;Ceremonial County, including Portsmouth and Southampton&quot;,
    &quot;type&quot;: &quot;boundary&quot;
  }
}
,
{
  &quot;type&quot;: &quot;area&quot;,
  &quot;id&quot;: 3603746024,
  &quot;tags&quot;: {
    &quot;boundary&quot;: &quot;statistical&quot;,
    &quot;name&quot;: &quot;Hampshire and Isle of Wight&quot;,
    &quot;ref:nuts:2&quot;: &quot;UKJ3&quot;,
    &quot;source&quot;: &quot;ONS_OpenData&quot;,
    &quot;type&quot;: &quot;boundary&quot;,
    &quot;wikipedia&quot;: &quot;en:NUTS of the United Kingdom&quot;
  }
}
&#10;  ]
}</code></pre>
<p>And from this is I can use code to go through the boundary admin_levels, in descending sequence, to give me:</p>
<p>New Forest, Hampshire, South East England, England, United Kingdom</p>
<p>which are exactly the details I was hoping to get from the is_in tag. So, I've started a process of doing this for all of the towns and cities, effectively adding my own 'is_in' tag to my application's database.</p>
<p>Here's some results from the process, with the node's is_in tag at the end (if it has one) to allows some comparison. The number at the beginning is the node's id for reference, e.g. <a href="https://www.openstreetmap.org/node/107775">https://www.openstreetmap.org/node/107775</a> for the first row.</p>
<pre><code>107775 - London: Greater London, England, United Kingdom [is_in=England, United Kingdom, UK, Great Britain, Europe]
204648 - Wellington: New Zealand [is_in=North Island, New Zealand]
273316 - Itajaí: Santa Catarina, South Region, Brazil [is_in=Santa Catarina, Brazil]
358309 - Leeds: Yorkshire and the Humber, England, United Kingdom [is_in=UK,United Kingdom, Yorkshire,West Yorkshire, Airedale]
441183 - Athens: Central section of Athens, Attica Periphery, Greece [is_in=Athina municipality,Attiki,Greece,EU]
671113 - Baltimore: Maryland, United States of America
1947201 - Bath: Bath &amp; North East Somerset, South West England, United Kingdom [is_in=Somerset, England, UK]
3216768 - St David&#39;s: Pembrokeshire, Wales, United Kingdom [is_in=Wales]
6968827 - Ljubljana: Osrednjeslovenska, Western Slovenia [is_in=Slovenia, Europe]
8087537 - Chester: Cheshire West and Chester, North West England, United Kingdom
9002746 - Charleroi: Hainaut, Wallonia (French Community), Belgium [is_in=Hainaut; Wallonie; Belgique; Europe]
9331795 - Limassol: Cyprus [is_in=Cyprus]
10021976 - Leicester: East Midlands, England, United Kingdom [is_in=Leicestershire, England, UK]
10671639 - Lincoln: Lincolnshire, East Midlands, England, United Kingdom
11094836 - Nyköping: Södermanlands län, Svealand, Sweden [is_in=Nyköping, Södermanland, Sweden, EU]
11127374 - Glasgow: Glasgow City, Scotland, United Kingdom [is_in=Scotland, UK]
11235057 - Norwich: Norfolk, East of England, United Kingdom [is_in=England, Norfolk]
12805909 - Oxford: Oxfordshire, South East England, United Kingdom [is_in=Oxfordshire, England, UK]
13707878 - Copenhagen: Capital Region of Denmark [is_in=Hovedstaden, Denmark, EU]
13766899 - Sydney: New South Wales, Australia
14446670 - Quezon City: Metro Manila, Philippines [is_in=Metro Manila]
14644309 - Iskenderun: Hatay, Mediterranean Region, Turkey [is_in=Turkey, Antakya]
15412058 - Helsingborg: Skåne län, Götaland, Sweden [is_in=Helsingborgs kommun, Skåne, Skåne län, Sweden]
16173235 - Mumbai: Maharashtra, India
16173236 - New Delhi: Delhi, India [is_in=National Capital Region, NCR, India]
16174445 - Pune: Maharashtra, India [is_in=India]
16175031 - Islamabad: Islamabad Capital Territory, Pakistan [is_in=Pakistan, Asia]
16175073 - Lahore: Punjab, Pakistan [is_in=Pakistan]
17193023 - Erlangen: Middle Franconia, Free State of Bavaria, Germany [is_in=Mittelfranken,Bayern,Bundesrepublik Deutschland,Europe]
17328659 - Vienna: Austria [is_in=Österreich,Europe]
17550787 - Pécs: Baranya megye, Southern Transdanubia, Hungary [is_in=Pécsi kistérség; Baranya megye; Dél-Dunántúl; Magyarország]
17721995 - Portsmouth: South East England, United Kingdom [is_in=Hampshire, England, UK]
17807753 - Paris: Ile-de-France, Metropolitan France
17857512 - Gloucester: Gloucestershire, South West England, United Kingdom [is_in=England, Gloucestershire]
17859918 - Coventry: West Midlands, England, United Kingdom
17861291 - Birmingham: West Midlands, England, United Kingdom [is_in=West Midlands, England, United Kingdom]
17898859 - Edinburgh: City of Edinburgh, Scotland, United Kingdom [is_in=Scotland, United Kingdom, UK, Great Britain, Europe]
17916174 - Canterbury: Kent, South East England, United Kingdom [is_in=Kent, England, UK]
17951258 - Peterborough: East of England, United Kingdom
17986274 - Plymouth: South West England, United Kingdom [is_in=Devon, England, UK]
18009959 - Exeter: Devon, South West England, United Kingdom [is_in=Devon, England, UK]
18063533 - Toronto: Ontario, Canada [is_in=Ontario, Canada]
18318938 - Hildesheim: Landkreis Hildesheim, Lower Saxony, Germany [is_in=Hildesheim,Niedersachsen,Bundesrepublik Deutschland,Europe]
18477455 - Bern: Verwaltungskreis Bern-Mittelland, Verwaltungsregion Bern-Mittelland, Switzerland [is_in=Bern-Mittelland,Schweiz,CH,Europe]
18886011 - Ottawa: Ontario, Canada [is_in=Ontario, Canada]</code></pre>
<p>So, my reason for posting this is that this raises some questions:</p>
<ol>
<li>Can my processing be improved? Should I look at Overpass areas other than the ones with a boundary and admin_level tag, perhaps? How would I determine the right sort sequence when I don't have an admin_level?</li>
<li>Should I consider sharing the results of my processing? Should I even consider using this to update the OSM central database, setting each place node with the is_in tags I have determined? I would have used a more standardised is_in tag if it had been available and so wonder if the OSM community could benefit somehow?</li>
<li>I'm really only considering English names, but am aware I'm working with Worldwide data. If this information is to be shared what additional processing should be added? I wonder if I can determine the language which is applicable to each node so I could use, for example, the name:es tags for a Spanish location rather than the name:en ones which I'm using currently?</li>
</ol>
<p>One thing nagging me is that I'm wondering why this approach hasn't been applied before. Map data is, by its very nature, a hierarchy of places within other places, so why is it necessary to have a free-form is_in tag to describe the hierarchy which already exists? I've read through <a href="https://wiki.openstreetmap.org/wiki/Key:is_in">https://wiki.openstreetmap.org/wiki/Key:is_in</a> and the discussion about boundary polygon making is_in redundant vs. is_in permitting 'simpler searching and easy disambiguation' and I strongly agree with the latter point; in my case having the is_in tag available would save a great deal of complex boundary processing by the Overpass API servers.</p>
<p>Thanks for any help or guidance you can offer.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mass_tagging" rel="tag" title="see questions tagged &#39;mass_tagging&#39;">mass_tagging</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-is_in" rel="tag" title="see questions tagged &#39;is_in&#39;">is_in</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jun '14, 13:35</strong></p>
<img src="https://secure.gravatar.com/avatar/68791600aba005984a3eddbd82f6c0ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Elliveny&#39;s gravatar image" />
<p><span>Elliveny</span><br />
<span class="score" title="66 reputation points">66</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Elliveny has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jun '14, 13:47</strong> </span></p>
</div>
</div>
<div id="comments-container-33711" class="comments-container">
<span id="33713"></span>
<div id="comment-33713" class="comment">
<div id="post-33713-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please don't ask multiple questions at once. You already seem to have noted that the use of the is_in tag is discouraged. It might be easier to process, but it is difficult to keep all the is_in tags including their full hierarchy up-to-date. Boundary polygons provide much more exact borders and are easier to maintain in the long run.</p>
</div>
<div id="comment-33713-info" class="comment-info">
<span class="comment-age">(05 Jun '14, 13:58)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="33715"></span>
<div id="comment-33715" class="comment">
<div id="post-33715-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, but it's difficult to avoid asking multiple questions when they relate to the same point.</p>
<p>I'm suggesting that if the is_in tag was set from the boundary polygons, then you avoid the need to do all that boundary processing in cases such as the one discussed in my question. If I have a planet file and an extract of the nodes representing the towns and cities I need to display, how should I determine the location name hierarchy? I think Nominatim is overkill for what I need. To ask a single question: I've found a way to achieve my requirements, is there a better approach though?</p>
</div>
<div id="comment-33715-info" class="comment-info">
<span class="comment-age">(05 Jun '14, 14:19)</span> <span class="comment-user userinfo">Elliveny</span>
</div>
</div>
</div>
<div id="comment-tools-33711" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33711-form-container" class="comment-form-container">
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

<span id="33712"></span>

<div id="answer-container-33712" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33712-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33712-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-33712-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Investigate "reverse geocoding" such as is possible with <a href="https://wiki.openstreetmap.org/wiki/Nominatim#Reverse_Geocoding_.2F_Address_lookup">Nominatim</a> or other services. The <a href="https://wiki.openstreetmap.org/wiki/Key:is_in"><code>is_in</code></a> tag is an old tag which is usually ignored or removed where boundary relations exist.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jun '14, 13:54</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-33712" class="comments-container">
<span id="33714"></span>
<div id="comment-33714" class="comment">
<div id="post-33714-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the suggestion. I have already worked with Nominatim and don't think it's suitable for this purpose. I'd need a local install of the whole planet file, which requires a heap of disk space and processing time. I could use an external Nominatim server, but my request volumes are likely to be too high. I could use an external Nominatim server against the city/town data and save the result, but I think this rather puts me back in the same place as I am with the Overpass API.</p>
</div>
<div id="comment-33714-info" class="comment-info">
<span class="comment-age">(05 Jun '14, 14:03)</span> <span class="comment-user userinfo">Elliveny</span>
</div>
</div>
<span id="33717"></span>
<div id="comment-33717" class="comment">
<div id="post-33717-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Given your comment on the is_in tag being old and usually ignored, I think it is also notable that Nominatim actually uses it when assessing the location name. See <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Development_overview:">https://wiki.openstreetmap.org/wiki/Nominatim/Development_overview:</a></p>
<p>"All items by name listed in the is_in are searched for within the current country (in no particular order)." and "During the indexing process an address is also calculated using the first feature found for each level. Where an is_in value is provided it is used to filter the address."</p>
</div>
<div id="comment-33717-info" class="comment-info">
<span class="comment-age">(05 Jun '14, 14:34)</span> <span class="comment-user userinfo">Elliveny</span>
</div>
</div>
</div>
<div id="comment-tools-33712" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33712-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33743"></span>

<div id="answer-container-33743" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33743-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33743-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33743-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe some more hints about reverse geocoding can be found at <a href="https://wiki.openstreetmap.org/wiki/Search_engines">Search_engines</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jun '14, 23:05</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-33743" class="comments-container">
&#10;</div>
<div id="comment-tools-33743" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33743-form-container" class="comment-form-container">
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

