+++
type = "question"
title = "tshark -E occurrence=a"
description = '''For my purposes, I record packets sent from radios stations that tell me their GPS position. The provider sometimes packages up 4 radio station reports into 1 packet. Basically, all the reports are exactly the same in terms of data, except for one or two fields where its ID# and position are differe...'''
date = "2012-05-23T09:11:00Z"
lastmod = "2012-05-31T10:26:00Z"
weight = 11265
keywords = [ "tshark" ]
aliases = [ "/questions/11265" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [tshark -E occurrence=a](/questions/11265/tshark-e-occurrencea)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11265-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11265-score" class="post-score" title="current number of votes">0</div><span id="post-11265-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>For my purposes, I record packets sent from radios stations that tell me their GPS position. The provider sometimes packages up 4 radio station reports into 1 packet. Basically, all the reports are exactly the same in terms of data, except for one or two fields where its ID# and position are different. All 4 reports are assembled and sent in one packet. I can easily decode and see the 4 distinct reports in that one packet while in the Wireshark GUI.</p><p>When I dump this to CSV format using <code>tshark</code>, I can only strip out the first report or the last report in the packet "correctly" using:</p><pre><code>tshark -E occurrence =a or ....=l</code></pre><p>I get one line of beautiful data showing all the values for each field for the first/last report. But if I say to give me ALL, it gives me each field from every report bunched together in a comma-separated format, all on one line as per the <code>tshark</code> documentation. So, it's working as stated; just not what I wanted.</p><p>If I can get the first report or last report to print correctly using the <code>f</code> or <code>a</code> switch, is there any way to get all the occurrences in that packet to print out like that? Each report pulled from the packet and printed on its own line?</p><p>I hope someone can follow along with what I am saying. I certainly appreciate any help. I'm assuming from how the documentation specifically states about printing multiple items at once for a single field that there is no workaround?</p><p><strong>UPDATE:</strong> I uploaded a <a href="https://www.cloudshark.org/captures/925cc4735bd0">sample</a> to <a href="http://cloudshark.org">cloudshark.org</a>. My packet of concern is the first packet for port 59951 and is 412 bytes long. There are actually 8 separate reports in this packet from 8 different radio stations. Wireshark might/will think it's a PROFINET-TIME protocol, which it's not. I have my own dissector for this for it's not this protocol. I can see all 8 reports fine in the GUI.</p><p>My <code>tshark</code> command is quite long for there is a lot coming in each report. As is, it works great, and I can bring it into Excel to display nicely as long as I choose first or last report in a packet.</p><pre><code>&quot;c:\program files\wireshark\tshark.exe&quot; -r filename.pcap -R &quot;(adsb.type == 33)&quot; -T fields -e frame.number -e frame.time_epoch -e adsb.svid.sac -e adsb.svid.domain -e adsb.svid.sic -e adsb.version.status -e adsb.version.number -e adsb.lti.unknown -e adsb.lti.version -e adsb.lti.1090 -e adsb.lti.uat -e adsb.lti.non_adsb -e adsb.toap.elapsed.whole -e adsb.toap.elapsed.frac -e adsb.toa.velocity.sign -e adsb.toav.elapsed.frac -e adsb.target_address.sv_type -e adsb.target_address.dup -e adsb.target_address.qualifier -e adsb.target_address.address -e adsb.iap.utc -e adsb.iap.nic -e adsb.iap.sil.sup -e adsb.iap.sil -e adsb.iap.nac_p -e adsb.iap.test -e adsb.iap.validation -e adsb.iap.nac_v.horiz -e adsb.iap.nic_baro -e adsb.gps_position.lat -e adsb.gps_position.lon -e adsb.altitude_pressure.resolution -e adsb.altitude_pressure.altitude -e adsb.velocity_air.vert_src -e adsb.velocity_air.scale -e adsb.velocity_air.ns_dir -e adsb.velocity_air.ns_vel -e adsb.velocity_air.ew_dir -e adsb.velocity_air.ew_vel -e adsb.velocity_air.vert_dir -e adsb.velocity_air.vert_vel -e adsb.mode3a.validity -e adsb.mode3a.code -e adsb.target_id -e adsb.emitter_category -e adsb.target_status.ident -e adsb.target_status.surveillance_status -e adsb.target_status.emergency_priority_code -e adsb.altitude_geometric -e adsb.op_mode_cap_code.capability_codes.tcas -e adsb.op_mode_cap_code.operational.ident -e adsb.op_mode_cap_code.operational.tcas.ra -e adsb.tomr.sign -e adsb.tomr.ns -e adsb.enh.val -e adsb.dqp.sda -e adsb.dsq.eq_type -e adsb.dsq.location_id -e adsb.dsq.instance -e adsb.target_state -E header=y -E separator=/t -E occurrence=f &gt; filemane.csv</code></pre><p>As I stated earlier, if I strip out the first report or last report of a packet, they come out great in <code>tshark</code>. If I ask for all the reports, I get one line of data with multiple used fields piled up together separated by commas. <code>adsb.dsq.location.id</code> is a field that is different in each report within the packet for this is the radio station ID. Rather than get 8 lines of data for the 8 reports in the packet, I get one line with any multiple-instance field (like this one) shown with comma separated values, such as: <code>15,16,24,356,etc.</code></p><p>I can list what the expected output is versus the actual output, if needed.</p><p>Here's the packet in Wireshark with my decoder clearly showing there are 8 reports within the packet. When I dump through <code>tshark</code> to csv, I can only choose to get first or last if I want one line per report. If I choose <code>-E occurrence=a</code>, I get ALL 8 reports on one line aggregated together. I can't figure out how to get them as 8 lines of output and not crammed together.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/xsample.JPG.pagespeed.ic.D7N-vvN8v0.jpg" alt="screenshot" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 May '12, 09:11</strong></p><img src="https://secure.gravatar.com/avatar/b363fb1dfec547bd68fa5e3eae8836a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike_P&#39;s gravatar image" /><p><span>Mike_P</span><br />
<span class="score" title="30 reputation points">30</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike_P has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 May '12, 12:32</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-11265" class="comments-container"><span id="11267"></span><div id="comment-11267" class="comment"><div id="post-11267-score" class="comment-score"></div><div class="comment-text"><p>What is the field you are extracting with tshark? Can you please post the whole tshark command?</p><p>BTW: can you post a small sample (3-4 packets) on <a href="http://cloudshark.org">cloudshark.org</a>?</p></div><div id="comment-11267-info" class="comment-info"><span class="comment-age">(23 May '12, 10:06)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="11273"></span><div id="comment-11273" class="comment"><div id="post-11273-score" class="comment-score"></div><div class="comment-text"><p>Based on the screenhot, you do have a dissector for ADS-B (Automatic Dependent Surveillance Broadcast). However, that code is not part of the official release, at least I cannot find it. Did you write that dissector yourself?</p></div><div id="comment-11273-info" class="comment-info"><span class="comment-age">(23 May '12, 11:04)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="11274"></span><div id="comment-11274" class="comment"><div id="post-11274-score" class="comment-score"></div><div class="comment-text"><p>Yes. I wrote it. Outside of my industry, I can't imagine anyone would be have any interest in dissecting these packets.</p></div><div id="comment-11274-info" class="comment-info"><span class="comment-age">(23 May '12, 11:06)</span> <span class="comment-user userinfo">Mike_P</span></div></div><span id="11275"></span><div id="comment-11275" class="comment"><div id="post-11275-score" class="comment-score"></div><div class="comment-text"><p>O.K., but without that dissector, nobody would be able to do any tests with your data ;-)) Can you provide that dissector?</p></div><div id="comment-11275-info" class="comment-info"><span class="comment-age">(23 May '12, 11:09)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="11276"></span><div id="comment-11276" class="comment"><div id="post-11276-score" class="comment-score"></div><div class="comment-text"><p>No problem. Its done in x86 or x64 Windows. How do I get the dll to you?</p></div><div id="comment-11276-info" class="comment-info"><span class="comment-age">(23 May '12, 11:12)</span> <span class="comment-user userinfo">Mike_P</span></div></div><span id="11277"></span><div id="comment-11277" class="comment not_top_scorer"><div id="post-11277-score" class="comment-score"></div><div class="comment-text"><p>upload it to <a href="http://depositfiles.com/">http://depositfiles.com/</a> and post the download link here. <strong>HINT</strong>: save the <strong>delete link</strong> as well. You will be able to delete the file later with that link.</p></div><div id="comment-11277-info" class="comment-info"><span class="comment-age">(23 May '12, 11:15)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="11281"></span><div id="comment-11281" class="comment not_top_scorer"><div id="post-11281-score" class="comment-score"></div><div class="comment-text"><p><a href="http://depositfiles.com/files/orgsmiyl5">http://depositfiles.com/files/orgsmiyl5</a></p></div><div id="comment-11281-info" class="comment-info"><span class="comment-age">(23 May '12, 11:19)</span> <span class="comment-user userinfo">Mike_P</span></div></div><span id="11282"></span><div id="comment-11282" class="comment not_top_scorer"><div id="post-11282-score" class="comment-score"></div><div class="comment-text"><p>I'll check it and <strong>I'll be back</strong> (I allways wanted to say that ;-))</p></div><div id="comment-11282-info" class="comment-info"><span class="comment-age">(23 May '12, 11:22)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="11283"></span><div id="comment-11283" class="comment not_top_scorer"><div id="post-11283-score" class="comment-score"></div><div class="comment-text"><p>Already, I thank you for your patience and efforts!!!</p></div><div id="comment-11283-info" class="comment-info"><span class="comment-age">(23 May '12, 11:23)</span> <span class="comment-user userinfo">Mike_P</span></div></div><span id="11284"></span><div id="comment-11284" class="comment not_top_scorer"><div id="post-11284-score" class="comment-score"></div><div class="comment-text"><p>unlike your screenshot, there is only one ADS-B report in the sample capture.</p></div><div id="comment-11284-info" class="comment-info"><span class="comment-age">(23 May '12, 11:29)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="11285"></span><div id="comment-11285" class="comment not_top_scorer"><div id="post-11285-score" class="comment-score"></div><div class="comment-text"><p>Do you mean 1 report in all 5 packets? Or you only see 1 report in the first packet? As you can see in my screen shot for the 1st packet, I expanded the Automatic Dependent Surveillance-Broadcast Protocol tree and inside are 8 reports. That's how its normally suppose to display. You don't see this when you run it with the dissector?</p><p>I had to DISABLE the PN-RT protocol under Analyze &gt; Protocols on my local Wireshark to get my dissector to display correctly.</p></div><div id="comment-11285-info" class="comment-info"><span class="comment-age">(23 May '12, 11:39)</span> <span class="comment-user userinfo">Mike_P</span></div></div><span id="11286"></span><div id="comment-11286" class="comment not_top_scorer"><div id="post-11286-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I had to DISABLE the PN-RT protocol</p></blockquote><p>O.K. that solved the problem. Hold on I'm looking at the data right now.</p></div><div id="comment-11286-info" class="comment-info"><span class="comment-age">(23 May '12, 11:50)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-11265" class="comment-tools"><span class="comments-showing"> showing 5 of 12 </span> <a href="#" class="show-all-comments-link">show 7 more comments</a></div><div class="clear"></div><div id="comment-11265-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="11287"></span>

<div id="answer-container-11287" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11287-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11287-score" class="post-score" title="current number of votes">1</div><span id="post-11287-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Mike_P has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>O.K. now I understand what you are looking for:</p><p>With "-E occurrence=a" the output looks like this:</p><blockquote><p><code>frame.number  frame.time_epoch    adsb.svid.sac   adsb.svid.domain    adsb.svid.sic</code><br />
<code>1 1.337.628.248.061.540.000   12,12,12,12,12,12,12,12 2,2,2,2,2,2,2,2 3,3,3,3,3,3,3,3</code><br />
<code>2 1.337.628.248.075.200.000   12,12,12,12,12  2,2,2,2,2   3,3,3,3,3</code><br />
</p></blockquote><p>while you would like to have it in this format (with reduced number of lines)</p><blockquote><p><code>frame.number  frame.time_epoch    adsb.svid.sac   adsb.svid.domain    adsb.svid.sic</code><br />
<code>1 1.337.628.248.061.540.000   12                   2           3</code><br />
<code>1 1.337.628.248.061.540.000   12                  2            3</code><br />
<code>1 1.337.628.248.061.540.000   12                      2            3</code><br />
<code>2 1.337.628.248.075.200.000   12                      2            3</code><br />
<code>2 1.337.628.248.075.200.000   12                      2            3</code><br />
<code>2 1.337.628.248.075.200.000   12                      2            3</code><br />
</p></blockquote><p>Unfortunately, this is not possible with the current version of wireshark, as the field print function just adds several instances separated by the "aggregator" character.</p><p>So, to solve your problem, you would have to script something with perl (or a similar scripting language).</p><p>Here's a Perl solution:</p><ul><li><p>Download TinyPerl (<a href="http://tinyperl.sourceforge.net/)">http://tinyperl.sourceforge.net/)</a> and unzip it to c:\tinyperl\tinyperl.</p></li><li><p>Save the code below to a file called c:\tinyperl\<a href="http://adsb-split.pl">adsb-split.pl</a>. <strong>WARNING</strong>: no guarantee for correctness !!</p></li><li><p>run this command</p></li></ul><blockquote><p><code>type output.csv | c:\tinyperl\tinyperl c:\tinyperl\adsb-split.pl &gt; splitted.csv</code></p></blockquote><p>Code:</p><pre><code>my $aggregator = &#39;,&#39;;
my $separator  = &#39;;&#39;;

while (&lt;STDIN&gt;) {

my $line = $_;
chomp($line);

my $f_index = 0;
my $max_subfields = 0;

my @fields;
my @results;

if ($line =~ /$aggregator/) {
    my @fields = split($separator,$line);

    foreach my $field (@fields) {
        $f_index++;

        if ($field =~ /$aggregator/) {
            @{$result[$f_index]-&gt;{multi}} = split($aggregator,$field);

            $n_subfields = @{$result[$f_index]-&gt;{multi}};
            if ($n_subfields &gt; $max_subfields) {
                $max_subfields = $n_subfields
            }
        } else {
            $result[$f_index]-&gt;{single} = $field;
        }
    }

    for my $n (1..$max_subfields) {

        foreach my $field (@result) {
            if (exists $field-&gt;{single}) {
                print $field-&gt;{single} . $separator;
            }
            if (exists $field-&gt;{multi}) {
                my $subfield = pop(@{$field-&gt;{multi}});
                print $subfield . $separator;
            }
        }
        print &quot;\n&quot;;
    }
 } else {
    print &quot;$line\n&quot;;
}
}</code></pre><p>Output Sample:</p><blockquote><p><code>frame.number;frame.time_epoch;adsb.svid.sac;adsb.svid.domain;adsb.svid.sic;adsb.version.status;adsb.version.number;adsb.lti.unknown;adsb.lti.version;adsb.lti.1090;adsb.lti.uat;adsb.lti.non_adsb;adsb.toap.elapsed.whole;adsb.toap.elapsed.frac;adsb.toa.velocity.sign;adsb.toav.elapsed.frac;adsb.target_address.sv_type;adsb.target_address.dup;adsb.target_address.qualifier;adsb.target_address.address;adsb.iap.utc;adsb.iap.nic;adsb.iap.sil.sup;adsb.iap.sil;adsb.iap.nac_p;adsb.iap.test;adsb.iap.validation;adsb.iap.nac_v.horiz;adsb.iap.nic_baro;adsb.gps_position.lat;adsb.gps_position.lon;adsb.altitude_pressure.resolution;adsb.altitude_pressure.altitude;adsb.velocity_air.vert_src;adsb.velocity_air.scale;adsb.velocity_air.ns_dir;adsb.velocity_air.ns_vel;adsb.velocity_air.ew_dir;adsb.velocity_air.ew_vel;adsb.velocity_air.vert_dir;adsb.velocity_air.vert_vel;adsb.mode3a.validity;adsb.mode3a.code;adsb.target_id;adsb.emitter_category;adsb.target_status.ident;adsb.target_status.surveillance_status;adsb.target_status.emergency_priority_code;adsb.altitude_geometric;adsb.op_mode_cap_code.capability_codes.tcas;adsb.op_mode_cap_code.operational.ident;adsb.op_mode_cap_code.operational.tcas.ra;adsb.tomr.sign;adsb.tomr.ns;adsb.enh.val;adsb.dqp.sda;adsb.dsq.eq_type;adsb.dsq.location_id;adsb.dsq.instance;adsb.target_state</code><br />
<code>1;1337628248.061542000;12;2;3;0;3;0;2;1;0;0;69701;57;0;127;0;0;1;0xfaafaa;1;10;0;3;10;0;3;9;0;1378549;12590923;0;8192;0;0;0;0;0;0;0;0;;;;;0;0;0;;;;;0;1918076928;0;2;13;16;3;5443853;</code><br />
<code>1;1337628248.061542000;12;2;3;0;3;0;2;1;0;0;69701;57;0;127;0;0;1;0xfaafaa;1;10;0;3;10;0;3;9;0;1378549;12590923;0;8192;0;0;0;0;0;0;0;0;;;;;0;0;0;;;;;0;1918076928;0;2;13;16;2;5443853;</code> <code>1;1337628248.061542000;12;2;3;0;3;0;2;1;0;0;69701;57;0;127;0;0;1;0xfaafaa;1;10;0;3;10;0;3;9;0;1378549;12590923;0;8192;0;0;0;0;0;0;0;0;;;;;0;0;0;;;;;0;1918076928;0;2;13;16;1;5443853;</code> <code>1;1337628248.061542000;12;2;3;0;3;0;2;1;0;0;69701;57;0;127;0;0;1;0xfaafaa;1;10;0;3;10;0;3;9;0;1378549;12590923;0;8192;0;0;0;0;0;0;0;0;;;;;0;0;0;;;;;0;1918076928;0;2;13;16;0;5443853;</code> <code>1;1337628248.061542000;12;2;3;0;3;0;2;1;0;0;69701;57;0;127;0;0;1;0xfaafaa;1;10;0;3;10;0;3;9;0;1399883;12471098;0;8192;0;0;0;0;0;0;0;0;;;;;0;0;0;;;;;0;1918076928;0;2;13;15;3;12480802;</code> <code>1;1337628248.061542000;12;2;3;0;3;0;2;1;0;0;69701;57;0;127;0;0;1;0xfaafaa;1;10;0;3;10;0;3;9;0;1399883;12471098;0;8192;0;0;0;0;0;0;0;0;;;;;0;0;0;;;;;0;1918076928;0;2;13;15;2;12480802;</code> <code>1;1337628248.061542000;12;2;3;0;3;0;2;1;0;0;69701;57;0;127;0;0;1;0xfaafaa;1;10;0;3;10;0;3;9;0;1399883;12471098;0;8192;0;0;0;0;0;0;0;0;;;;;0;0;0;;;;;0;1918076928;0;2;13;15;1;12480802;</code> <code>1;1337628248.061542000;12;2;3;0;3;0;2;1;0;0;69701;57;0;127;0;0;1;0xfaafaa;1;10;0;3;10;0;3;9;0;1399883;12471098;0;8192;0;0;0;0;0;0;0;0;;;;;0;0;0;;;;;0;1918076928;0;2;13;15;0;12480802;</code> <code>2;1337628248.075203000;12;2;3;0;3;0;2;1;0;0;69701;57;0;127;0;0;1;0xfaafaa;1;10;0;3;10;0;3;9;0;1415326;12608481;0;8192;0;0;0;0;0;0;0;0;;;;;0;0;0;;;;;0;1918076928;0;2;13;341;0;15150739;</code> <code>2;1337628248.075203000;12;2;3;0;3;0;2;1;0;0;69701;57;0;127;0;0;1;0xfaafaa;1;10;0;3;10;0;3;9;0;1402027;12555896;0;8192;0;0;0;0;0;0;0;0;;;;;0;0;0;;;;;0;1918076928;0;2;13;338;3;16390297;</code> <code>2;1337628248.075203000;12;2;3;0;3;0;2;1;0;0;69701;57;0;127;0;0;1;0xfaafaa;1;10;0;3;10;0;3;9;0;1402027;12555896;0;8192;0;0;0;0;0;0;0;0;;;;;0;0;0;;;;;0;1918076928;0;2;13;338;2;16390297;</code> <code>2;1337628248.075203000;12;2;3;0;3;0;2;1;0;0;69701;57;0;127;0;0;1;0xfaafaa;1;10;0;3;10;0;3;9;0;1402027;12555896;0;8192;0;0;0;0;0;0;0;0;;;;;0;0;0;;;;;0;1918076928;0;2;13;338;1;16390297;</code> <code>2;1337628248.075203000;12;2;3;0;3;0;2;1;0;0;69701;57;0;127;0;0;1;0xfaafaa;1;10;0;3;10;0;3;9;0;1402027;12555896;0;8192;0;0;0;0;0;0;0;0;;;;;0;0;0;;;;;0;1918076928;0;2;13;338;0;16390297;</code> <code>3;1337628248.086516000;12;2;3;0;3;0;2;1;0;0;69701;57;0;127;0;0;1;0xfaafaa;1;10;0;3;10;0;3;9;0;1436506;12557234;0;8192;0;0;0;0;0;0;0;0;;;;;0;0;0;;;;;0;1918076928;0;2;13;357;0;9940084;</code> <code>3;1337628248.086516000;12;2;3;0;3;0;2;1;0;0;69701;57;0;127;0;0;1;0xfaafaa;1;10;0;3;10;0;3;9;0;1416410;12512643;0;8192;0;0;0;0;0;0;0;0;;;;;0;0;0;;;;;0;1918076928;0;2;13;356;0;5266782;</code> <code>4;1337628248.204514000;12;2;3;0;3;0;1;1;0;0;69701;64;0;4;0;0;0;0xa9ea08;0;9;0;2;9;0;3;10;1;1333652;12560133;2;137;0;0;1;609;0;85;1;1;1;2279;40:83:70:cf:60:60;7;0;0;0;592;0;0;0;0;536973395;0;0;13;16;2;5443998</code></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '12, 12:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 May '12, 03:31</strong> </span></p></div></div><div id="comments-container-11287" class="comments-container"><span id="11492"></span><div id="comment-11492" class="comment"><div id="post-11492-score" class="comment-score"></div><div class="comment-text"><p>I tried using this Perl code, but it gives me it one value per line unlike your sample output above. I'm not at all familiar with Perl, so I have no idea what I should tweak to fix it. I'm grateful you even included any sample code and I realize there was no guarantee it would work. Any ideas?</p></div><div id="comment-11492-info" class="comment-info"><span class="comment-age">(31 May '12, 10:08)</span> <span class="comment-user userinfo">Mike_P</span></div></div><span id="11496"></span><div id="comment-11496" class="comment"><div id="post-11496-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Any ideas?</p></blockquote><p>Can you please upload the input for the perl script somewhere (One Click Hoster)?</p><p>FURTHERMORE: I recommend to use the Lua script posted by helloworld. It does not need additional software on the computer and it's much easier to understand. However, you need to extend it with all your fields, as the posted script is just a example (a working one)!</p></div><div id="comment-11496-info" class="comment-info"><span class="comment-age">(31 May '12, 10:26)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-11287" class="comment-tools"></div><div class="clear"></div><div id="comment-11287-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11295"></span>

<div id="answer-container-11295" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11295-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11295-score" class="post-score" title="current number of votes">1</div><span id="post-11295-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use Wireshark's <a href="http://www.wireshark.org/docs/wsug_html_chunked/wsluarm.html">Lua API</a> to print info similar to <code>tshark</code>'s output.</p><h4 id="test.lua">test.lua:</h4><pre><code>local filter = &#39;ads-b&#39; -- use display filter syntax here
local tap = Listener.new(nil, filter)

-- declare field extractors for your named fields
local f_sac = Field.new(&#39;adsb.svid.sac&#39;)
local f_domain = Field.new(&#39;adsb.svid.domain&#39;)
local f_sic = Field.new(&#39;adsb.svid.sic&#39;)

-- converts a Field into an array of FieldInfo instances
local function toarray(fld)
    local arr = {}
    for _,x in ipairs({ fld() }) do
        arr[1 + #arr] = x
    end
    return arr
end

-- function called for each packet that matches filter defined above
function tap.packet(pinfo)
    local sac       = toarray(f_sac)
    local domain    = toarray(f_domain)
    local sic       = toarray(f_sic)

    -- For each instance of &#39;adsb.svid.sac&#39;, print a line that contains:
    --    {frame.number} {frame.time_epoch} {adsb.svid.sac} {adsb.svid.domain} {adsb.svid.sic}
    for i=1,#sac do

        -- print() here prints each argument delimited by tabs
        print(
            pinfo.number, -- equivalent to frame.number
            pinfo.abs_ts, -- equivalent to frame.time_epoch
            sac[i],
            domain[i],
            sic[i]
        )

        -- You can also change the format to match tshark&#39;s output
        -- (space-delimited) by using string.format() (which is like 
        -- C&#39;s printf):
        --
        --print(string.format(&quot;%d %.8f %s %s %s&quot;,
        --      pinfo.number, -- equivalent to frame.number
        --      pinfo.abs_ts, -- equivalent to frame.time_epoch
        --      sac[i],
        --      domain[i],
        --      sic[i]
        --))

    end
end</code></pre><h4 id="usage">Usage:</h4><pre><code> tshark -q -r file.pcap -Xlua_script:test.lua</code></pre><p><em>This command assumes <code>file.pcap</code> and <code>test.lua</code> are in the current directory. Use absolute paths here if necessary.</em></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '12, 13:52</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 May '12, 04:01</strong> </span></p></div></div><div id="comments-container-11295" class="comments-container"><span id="11303"></span><div id="comment-11303" class="comment"><div id="post-11303-score" class="comment-score"></div><div class="comment-text"><p>the lua code works pretty well. However, tshark will print it's default output after the listener output for every frame.</p><p>Can I suppress the default output?</p><p>One option would be to print a field (-T fields) that is not available in the capture file. Are there better ways?</p></div><div id="comment-11303-info" class="comment-info"><span class="comment-age">(24 May '12, 01:25)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="11306"></span><div id="comment-11306" class="comment"><div id="post-11306-score" class="comment-score"></div><div class="comment-text"><p>Yes, the <code>-q</code> flag accomplishes this. I updated the usage.</p></div><div id="comment-11306-info" class="comment-info"><span class="comment-age">(24 May '12, 04:02)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="11307"></span><div id="comment-11307" class="comment"><div id="post-11307-score" class="comment-score"></div><div class="comment-text"><p>sometimes, the obvious things are hard to find :-)</p></div><div id="comment-11307-info" class="comment-info"><span class="comment-age">(24 May '12, 04:27)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="11308"></span><div id="comment-11308" class="comment"><div id="post-11308-score" class="comment-score"></div><div class="comment-text"><p>...and easy to forget ;)</p></div><div id="comment-11308-info" class="comment-info"><span class="comment-age">(24 May '12, 04:47)</span> <span class="comment-user userinfo">helloworld</span></div></div></div><div id="comment-tools-11295" class="comment-tools"></div><div class="clear"></div><div id="comment-11295-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11288"></span>

<div id="answer-container-11288" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11288-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11288-score" class="post-score" title="current number of votes">0</div><span id="post-11288-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Nope, there is no workaround for this (apart from changing the code). But you can always use 'tshark -V' to get the whole tree. Or (even more bloated) 'tshark -T pdml' to get the XML output, which will be easier to parse.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '12, 12:10</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-11288" class="comments-container"><span id="11289"></span><div id="comment-11289" class="comment"><div id="post-11289-score" class="comment-score"></div><div class="comment-text"><p>Thank you gentlemen!! I was thinking this was going to be the answer as the documentation states this is how its designed to work. I was just hoping I was missing some secret switch to get around it. :)</p><p>I thank you for looking into this situation and promptly getting me a definitive answer.</p></div><div id="comment-11289-info" class="comment-info"><span class="comment-age">(23 May '12, 12:12)</span> <span class="comment-user userinfo">Mike_P</span></div></div></div><div id="comment-tools-11288" class="comment-tools"></div><div class="clear"></div><div id="comment-11288-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

