+++
type = "question"
title = "Connect Garmin to Mapsource on Ubuntu"
description = '''I have installed MapSource 6.16.3 in wine 1.3.22 on Ubuntu 11.04, the installation worked, and I&#x27;m able to view maps and all those things, but I have installed MapSource mainly to send maps (OpenMtbMap to be specific) to my Garmin GPS (Nüvi 1390). According to the different tutorials and tips that I...'''
date = "2011-06-30T15:32:00Z"
lastmod = "2011-07-01T20:42:00Z"
weight = 6110
keywords = [ "mapsource", "device", "garmin", "ubuntu" ]
aliases = [ "/questions/6110" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Connect Garmin to Mapsource on Ubuntu](/questions/6110/connect-garmin-to-mapsource-on-ubuntu)

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
<span id="post-6110-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6110-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-6110-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have installed MapSource 6.16.3 in wine 1.3.22 on Ubuntu 11.04, the installation worked, and I'm able to view maps and all those things, but I have installed MapSource mainly to send maps (OpenMtbMap to be specific) to my Garmin GPS (Nüvi 1390).</p>
<p>According to the different tutorials and tips that I have read, I should see my GPS as /dev/ttyUSB0, but when I plug the USB in, I only see it as an extra HDD. This is my /dev before I plugin the GPS (sorry for the mess, but I cannot get the formatting right):</p>
<pre><code>agpgart      mem             sda2      tty28  tty60  ttyS6
autofs       net             sda5      tty29  tty61  ttyS7
block        network_latency     sda6      tty3   tty62  ttyS8
bsg              network_throughput  sda7      tty30  tty63  ttyS9
btrfs-control    null            sda8      tty31  tty7   uinput
bus              oldmem          sg0       tty32  tty8   urandom
cdrom        pktcdvd         sg1       tty33  tty9   usbmon0
cdrw         port            shm       tty34  ttyprintk  usbmon1
char         ppp             snapshot  tty35  ttyS0  usbmon2
console      psaux           snd       tty36  ttyS1  v4l
core         ptmx            sr0       tty37  ttyS10     vcs
cpu              pts             stderr    tty38  ttyS11     vcs1
cpu_dma_latency      ram0            stdin     tty39  ttyS12     vcs2
disk         ram1            stdout    tty4   ttyS13     vcs3
dri              ram10           tty       tty40  ttyS14     vcs4
dvd              ram11           tty0      tty41  ttyS15     vcs5
dvdrw        ram12           tty1      tty42  ttyS16     vcs6
ecryptfs             ram13           tty10     tty43  ttyS17     vcs63
fb0              ram14           tty11     tty44  ttyS18     vcs8
fd               ram15           tty12     tty45  ttyS19     vcsa
full         ram2            tty13     tty46  ttyS2  vcsa1
fuse         ram3            tty14     tty47  ttyS20     vcsa2
hpet         ram4            tty15     tty48  ttyS21     vcsa3
input        ram5            tty16     tty49  ttyS22     vcsa4
kmsg         ram6            tty17     tty5   ttyS23     vcsa5
log              ram7            tty18     tty50  ttyS24     vcsa6
loop0        ram8            tty19     tty51  ttyS25     vcsa63
loop1        ram9            tty2      tty52  ttyS26     vcsa8
loop2        random          tty20     tty53  ttyS27     vga_arbiter
loop3        rfkill          tty21     tty54  ttyS28     video0
loop4        root            tty22     tty55  ttyS29     zero
loop5        rtc             tty23     tty56  ttyS3
loop6        rtc0            tty24     tty57  ttyS30
loop7        scd0            tty25     tty58  ttyS31
mapper       sda             tty26     tty59  ttyS4
mcelog       sda1            tty27     tty6   ttyS5</code></pre>
<p>And this is after I have plugged in my GPS:</p>
<pre><code>agpgart      mem             sda2      tty24  tty57  ttyS30
autofs       net             sda5      tty25  tty58  ttyS31
block        network_latency     sda6      tty26  tty59  ttyS4
bsg              network_throughput  sda7      tty27  tty6   ttyS5
btrfs-control    null            sda8      tty28  tty60  ttyS6
bus              oldmem          sdb       tty29  tty61  ttyS7
cdrom        pktcdvd         sdc       tty3   tty62  ttyS8
cdrw         port            sg0       tty30  tty63  ttyS9
char         ppp             sg1       tty31  tty7   uinput
console      psaux           sg2       tty32  tty8   urandom
core         ptmx            sg3       tty33  tty9   usbmon0
cpu              pts             shm       tty34  ttyprintk  usbmon1
cpu_dma_latency      ram0            snapshot  tty35  ttyS0  usbmon2
disk         ram1            snd       tty36  ttyS1  v4l
dri              ram10           sr0       tty37  ttyS10     vcs
dvd              ram11           stderr    tty38  ttyS11     vcs1
dvdrw        ram12           stdin     tty39  ttyS12     vcs2
ecryptfs             ram13           stdout    tty4   ttyS13     vcs3
fb0              ram14           tty       tty40  ttyS14     vcs4
fd               ram15           tty0      tty41  ttyS15     vcs5
full         ram2            tty1      tty42  ttyS16     vcs6
fuse         ram3            tty10     tty43  ttyS17     vcs63
hpet         ram4            tty11     tty44  ttyS18     vcs8
input        ram5            tty12     tty45  ttyS19     vcsa
kmsg         ram6            tty13     tty46  ttyS2  vcsa1
log              ram7            tty14     tty47  ttyS20     vcsa2
loop0        ram8            tty15     tty48  ttyS21     vcsa3
loop1        ram9            tty16     tty49  ttyS22     vcsa4
loop2        random          tty17     tty5   ttyS23     vcsa5
loop3        rfkill          tty18     tty50  ttyS24     vcsa6
loop4        root            tty19     tty51  ttyS25     vcsa63
loop5        rtc             tty2      tty52  ttyS26     vcsa8
loop6        rtc0            tty20     tty53  ttyS27     vga_arbiter
loop7        scd0            tty21     tty54  ttyS28     video0
mapper       sda             tty22     tty55  ttyS29     zero
mcelog       sda1            tty23     tty56  ttyS3</code></pre>
<p>As you see, there are some extra devices (most notably sdb and sdc), but nothing that looks like /dev/ttyUSB0. Some tips also suggest <code>sudo modprobe garmin_gps</code> to make it appear as /dev/ttyUSB0, but that did change nothing at all.</p>
<p>Once I have it as ttyUSB0, I should make a softlink from the com0 port of Wine to that device. Than I could connect MapSource to the GPS. But since I don't have ttyUSB0, I can't make the softlink.</p>
<p>So if anyone can make it appear as /dev/ttyUSB0 or knows another way to put maps on it (without removing the maps that already are on it), please tell me.</p>
<p><strong>TLDR</strong>: My GPS should show as /dev/ttyUSB0, but it doesn't.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapsource" rel="tag" title="see questions tagged &#39;mapsource&#39;">mapsource</span> <span class="post-tag tag-link-device" rel="tag" title="see questions tagged &#39;device&#39;">device</span> <span class="post-tag tag-link-garmin" rel="tag" title="see questions tagged &#39;garmin&#39;">garmin</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jun '11, 15:32</strong></p>
<img src="https://secure.gravatar.com/avatar/1fe9a0c696a5000fb304ababea9f83af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanderd17&#39;s gravatar image" />
<p><span>Sanderd17</span><br />
<span class="score" title="1111 reputation points"><span>1.1k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanderd17 has 15 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-6110" class="comments-container">
&#10;</div>
<div id="comment-tools-6110" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6110-form-container" class="comment-form-container">
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

<span id="6114"></span>

<div id="answer-container-6114" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6114-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6114-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-6114-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not sure which tutorials you are referring to. Older Garmin devices worked using Garmin USB protocol (so would show up as /dev/ttyUSB0), but most recent models only work in USB Mass Storage Mode (so just show up as a removable drive). See this list on the wiki: <a href="https://wiki.openstreetmap.org/wiki/OSM_Map_On_Garmin/Mass_Storage_Mode">Garmin USB Mass storage mode</a></p>
<p>I'm not familiar with that model Nuvi, but it sounds like it only works in mass storage mode. But MapSource should still be able to upload to it (assuming Wine can see it as a removable drive). Just select some maps, then click "Send to Device". MapSource should detect the drive, and let you send the maps to it.</p>
<p>Note by default when you upload a map set from MapSource, it will delete any maps that were previously on the device. So if you have any maps on it you want to keep, it would be a good idea to back them up first. Its probably easiest just to take a copy of everything on the removable drive.</p>
<p>Also note you can upload maps without using MapSource. For Garmins that work in mass storage mode, you just need to copy a gmapsupp.img file to the correct directory on the removable drive. For most devices, you need to copy it to a directory named "Garmin", but apparently for the Nuvi 1390 it needs to be in a directory named "Map" (according to that list in the wiki). You might be able to use several .img files with different names, so you can use multiple map sets.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jun '11, 18:05</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-6114" class="comments-container">
<span id="6117"></span>
<div id="comment-6117" class="comment">
<div id="post-6117-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was referring to the installation help on the Wine DB, and some thread in the Ubuntu forums. Apparently for older Garmins.</p>
<p>Since you say they are only seen as a mass storage device, I tried adding a Station D: in the wine settings which would refer to /media/GARMIN, where /dev/sdb is mounted. But that didn't work. When I click the "search devices" button, it immediately says that no devices are found.</p>
<p>And where do I find the gmapsupp.img file? If I unpack a .exe file from openmtbmap, I see serveral img files and a bat script called "create_gmapsupp.img.bat".</p>
<p>But thanks for the tips.</p>
</div>
<div id="comment-6117-info" class="comment-info">
<span class="comment-age">(30 Jun '11, 19:42)</span> <span class="comment-user userinfo">Sanderd17</span>
</div>
</div>
<span id="6120"></span>
<div id="comment-6120" class="comment">
<div id="post-6120-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It seems MapSource will only detect USB flash drives, it doesn't detect hard drives etc. I don't know if there's any setting in Wine to make a drive appear to be a USB drive?</p>
<p>For a gmapsupp.img file: you can use Mkgmap to combine several img files into a gmapsupp.img file. There is instructions for how to do this for Openmtbmap here: <a href="http://openmtbmap.org/tutorials/send-maps-to-your-gps/mkgmap/">http://openmtbmap.org/tutorials/send-maps-to-your-gps/mkgmap/</a></p>
<p>Or there are other websites for OSM Garmin maps which can provide a ready made gmapsupp.img file. One option for worldwide maps is <a href="http://garmin.openstreetmap.nl/">http://garmin.openstreetmap.nl/</a></p>
</div>
<div id="comment-6120-info" class="comment-info">
<span class="comment-age">(30 Jun '11, 20:44)</span> <span class="comment-user userinfo">Vclaw</span>
</div>
</div>
<span id="6144"></span>
<div id="comment-6144" class="comment">
<div id="post-6144-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I also asked it on the Ubuntu forums, and the one step I was missing was setting the device type to "floppy" in the extra settings.</p>
<p>See here: <a href="http://ubuntuforums.org/showthread.php?p=11002538#post11002538">http://ubuntuforums.org/showthread.php?p=11002538#post11002538</a></p>
<p>If you edit your answer, I will mark it as the accepted answer.</p>
</div>
<div id="comment-6144-info" class="comment-info">
<span class="comment-age">(01 Jul '11, 20:42)</span> <span class="comment-user userinfo">Sanderd17</span>
</div>
</div>
</div>
<div id="comment-tools-6114" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6114-form-container" class="comment-form-container">
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

