+++
type = "question"
title = "Error compiling on Solaris 10 - Makefile unexpected end of line"
description = '''My first attempt at installing Wireshark on a Solaris 10 x86 system was to download the packages from Sunfreeware.com (including all dependencies) and install them. There are some library errors with libwireshark.so.1 where a dependent library (libgnutls.so.26 (&#x27;GNU_1_4&#x27;)) isn&#x27;t found. I&#x27;m not findi...'''
date = "2012-05-07T13:53:00Z"
lastmod = "2012-05-07T16:01:00Z"
weight = 10749
keywords = [ "compile", "solaris", "makefile" ]
aliases = [ "/questions/10749" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Error compiling on Solaris 10 - Makefile unexpected end of line](/questions/10749/error-compiling-on-solaris-10-makefile-unexpected-end-of-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10749-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My first attempt at installing Wireshark on a Solaris 10 x86 system was to download the packages from <a href="http://Sunfreeware.com">Sunfreeware.com</a> (including all dependencies) and install them. There are some library errors with libwireshark.so.1 where a dependent library (libgnutls.so.26 ('GNU_1_4')) isn't found. I'm not finding much on that issue so I decided to try and compile Wireshark myself.<br />
<br />
Here is the configure output..<br />
</p><p>Script started on Mon May 07 16:38:22 2012<br />
johndeere {root}# ./configure<br />
checking build system type... i386-pc-solaris2.10<br />
checking host system type... i386-pc-solaris2.10<br />
checking target system type... i386-pc-solaris2.10<br />
checking for a BSD-compatible install... ./install-sh -c<br />
checking whether build environment is sane... yes<br />
checking for gawk... no<br />
checking for mawk... no<br />
checking for nawk... nawk<br />
checking whether make sets $(MAKE)... yes<br />
checking how to create a ustar tar archive... gnutar<br />
checking for gcc... gcc<br />
checking whether the C compiler works... yes<br />
checking for C compiler default output file name... a.out<br />
checking for suffix of executables...<br />
checking whether we are cross compiling... no<br />
checking for suffix of object files... o<br />
checking whether we are using the GNU C compiler... yes<br />
checking whether gcc accepts -g... yes<br />
checking for gcc option to accept ISO C89... none needed<br />
checking for style of include used by make... GNU<br />
checking dependency style of gcc... gcc3<br />
checking whether gcc and cc understand -c and -o together... yes<br />
checking for g++... g++<br />
checking whether we are using the GNU C++ compiler... yes<br />
checking whether g++ accepts -g... yes<br />
checking dependency style of g++... gcc3<br />
checking how to run the C preprocessor... gcc -E<br />
checking for a sed that does not truncate output... /usr/local/bin/sed<br />
checking for grep that handles long lines and -e... /usr/sfw/bin/ggrep<br />
checking for egrep... /usr/sfw/bin/ggrep -E<br />
checking for fgrep... /usr/sfw/bin/ggrep -F<br />
checking for ld used by gcc... /usr/ccs/bin/ld<br />
checking if the linker (/usr/ccs/bin/ld) is GNU ld... no<br />
checking for BSD- or MS-compatible name lister (nm)... /usr/ccs/bin/nm -p<br />
checking the name lister (/usr/ccs/bin/nm -p) interface... BSD nm<br />
checking whether ln -s works... yes<br />
checking the maximum length of command line arguments... 786240<br />
checking whether the shell understands some XSI constructs... yes<br />
checking whether the shell understands "+="... yes<br />
checking for /usr/ccs/bin/ld option to reload object files... -r<br />
checking for objdump... no<br />
checking how to recognize dependent libraries... pass_all<br />
checking for ar... ar<br />
checking for strip... strip<br />
checking for ranlib... ranlib<br />
checking command to parse /usr/ccs/bin/nm -p output from gcc object... ok<br />
checking for ANSI C header files... yes<br />
checking for sys/types.h... yes<br />
checking for sys/stat.h... yes<br />
checking for stdlib.h... yes<br />
checking for string.h... yes<br />
checking for memory.h... yes<br />
checking for strings.h... yes<br />
checking for inttypes.h... yes<br />
checking for stdint.h... yes<br />
checking for unistd.h... yes<br />
checking for dlfcn.h... yes<br />
checking whether we are using the GNU C++ compiler... (cached) yes<br />
checking whether g++ accepts -g... (cached) yes<br />
checking dependency style of g++... (cached) gcc3<br />
checking how to run the C++ preprocessor... g++ -E<br />
checking for objdir... .libs<br />
checking if gcc supports -fno-rtti -fno-exceptions... no<br />
checking for gcc option to produce PIC... -fPIC -DPIC<br />
checking if gcc PIC flag -fPIC -DPIC works... yes<br />
checking if gcc static flag -static works... no<br />
checking if gcc supports -c -o file.o... yes<br />
checking if gcc supports -c -o file.o... (cached) yes<br />
checking whether the gcc linker (/usr/ccs/bin/ld) supports shared libraries... yes<br />
checking whether -lc should be explicitly linked in... yes<br />
checking dynamic linker characteristics... solaris2.10 <a href="http://ld.so">ld.so</a><br />
checking how to hardcode library paths into programs... immediate<br />
checking for shl_load... no<br />
checking for shl_load in -ldld... no<br />
checking for dlopen... yes<br />
checking whether a program can dlopen itself... yes<br />
checking whether a statically linked program can dlopen itself... yes<br />
checking whether stripping libraries is possible... no<br />
checking if libtool supports shared libraries... yes<br />
checking whether to build shared libraries... yes<br />
checking whether to build static libraries... no<br />
checking for ld used by g++... /usr/ccs/bin/ld<br />
checking if the linker (/usr/ccs/bin/ld) is GNU ld... no<br />
checking whether the g++ linker (/usr/ccs/bin/ld) supports shared libraries... yes<br />
checking for g++ option to produce PIC... -fPIC -DPIC<br />
checking if g++ PIC flag -fPIC -DPIC works... yes<br />
checking if g++ static flag -static works... no<br />
checking if g++ supports -c -o file.o... yes<br />
checking if g++ supports -c -o file.o... (cached) yes<br />
checking whether the g++ linker (/usr/ccs/bin/ld) supports shared libraries... yes<br />
checking dynamic linker characteristics... solaris2.10 <a href="http://ld.so">ld.so</a><br />
checking how to hardcode library paths into programs... immediate<br />
checking for perl... /usr/bin/perl<br />
checking for bison... bison -y<br />
checking for bison... /usr/sfw/bin/bison<br />
checking for flex... flex<br />
checking lex output file root... lex.yy<br />
checking lex library... -lfl<br />
checking whether yytext is a pointer... yes<br />
checking for flex... /usr/sfw/bin/flex<br />
checking for pod2man... /usr/local/bin/pod2man<br />
checking for pod2html... /usr/local/bin/pod2html<br />
checking for xdg-open... no<br />
checking for htmlview... no<br />
checking for python... /usr/local/bin/python<br />
checking for doxygen... no<br />
checking for doxygen... no<br />
checking for special C compiler options needed for large files... no<br />
checking for _FILE_OFFSET_BITS value needed for large files... 64<br />
checking for pkg-config... /usr/local/bin/pkg-config<br />
checking pkg-config is at least version 0.9.0... yes<br />
checking for LIBGNUTLS... yes<br />
gnuTLS found, enabling ssl decryption<br />
checking for libgcrypt-config... /usr/local/bin/libgcrypt-config<br />
checking for LIBGCRYPT - version &gt;= 1.1.92... yes<br />
libgcrypt found, enabling ipsec decryption<br />
checking for libsmi &gt;= 2... not found<br />
checking for xsltproc... /usr/bin/xsltproc<br />
checking for xsltproc... yes<br />
checking for xmllint... /usr/bin/xmllint<br />
checking for xmllint... yes<br />
checking for fop... no<br />
checking for fop... no<br />
checking for elinks... no<br />
checking for elinks... no<br />
checking for lynx... no<br />
checking for lynx... no<br />
checking for hhc.exe... no<br />
checking for hhc.exe... no<br />
checking for pkgproto... yes<br />
checking for pkgmk... yes<br />
checking for pkgtrans... yes<br />
checking for rpm... no<br />
checking for dpkg-buildpackage... no<br />
checking for xcodebuild... no<br />
checking for hdiutil... no<br />
checking for bless... no<br />
checking whether we can add -Wall -W to CFLAGS... yes<br />
checking whether we can add -Wextra to CFLAGS... yes<br />
checking whether we can add -Wdeclaration-after-statement to CFLAGS... yes<br />
checking whether we can add -Wendif-labels to CFLAGS... yes<br />
checking whether we can add -Wpointer-arith to CFLAGS... yes<br />
checking whether we can add -Wno-pointer-sign to CFLAGS... no<br />
checking whether we can add -Warray-bounds to CFLAGS... no<br />
checking whether we can add -Wcast-align to CFLAGS... yes<br />
checking whether we can add -Wformat-security to CFLAGS... yes<br />
checking whether we can add -fexcess-precision=fast to CFLAGS... no<br />
checking whether we can add -Wl,--as-needed to LDFLAGS... no<br />
checking whether we should treat compiler warnings as errors... no<br />
checking for platform-specific compiler flags... GCC on Solaris - added -Wno-return-type -DFUNCPROTO=15<br />
checking for platform-specific linker flags... none needed<br />
checking whether to use NONE for headers and libraries... no<br />
checking whether to use /usr/local for headers and libraries... yes<br />
checking for LD_LIBRARY_PATH... no -- this may be a problem in a few seconds<br />
checking for GNU sed as first sed in PATH... yes<br />
checking if profile builds must be generated... no<br />
checking for pkg-config... /usr/local/bin/pkg-config<br />
checking for GTK+ - version &gt;= 2.4.0... yes (version 2.12.0)<br />
checking for pkg-config... (cached) /usr/local/bin/pkg-config<br />
checking for GLIB - version &gt;= 2.4.0... yes (version 2.18.3)<br />
checking for GLIB - version &gt;= 2.14.0... yes<br />
checking whether GLib supports loadable modules... yes<br />
checking whether dladdr can be used to find the pathname of an executable... yes<br />
checking whether to use OS X integration functions... yes<br />
checking for gtk_osxapplication_set_menu_bar in -ligemacintegration... no<br />
checking for ige_mac_menu_set_menu_bar in -lGtk... no<br />
checking for ige_mac_menu_set_menu_bar in -ligemacintegration... no<br />
checking for gethostbyname... no<br />
checking for gethostbyname in -lnsl... yes<br />
checking for connect... no<br />
checking for connect in -lsocket... yes<br />
checking whether to use libpcap for packet capture... yes<br />
checking for pcap-config... /usr/local/bin/pcap-config<br />
checking for broken pcap-config... no<br />
checking pcap.h usability... yes<br />
checking pcap.h presence... yes<br />
checking for pcap.h... yes<br />
checking for pcap_open_dead... yes<br />
checking for pcap_freecode... yes<br />
checking whether pcap_breakloop is present... yes<br />
checking whether pcap_findalldevs is present and usable... yes<br />
checking for pcap_datalink_val_to_name... yes<br />
checking for pcap_datalink_name_to_val... yes<br />
checking for pcap_datalink_val_to_description... yes<br />
checking for pcap_list_datalinks... yes<br />
checking for pcap_set_datalink... yes<br />
checking for pcap_lib_version... yes<br />
checking for pcap_get_selectable_fd... yes<br />
checking for pcap_free_datalinks... yes<br />
checking for pcap_create... yes<br />
checking for bpf_image... yes<br />
checking whether to build dumpcap... yes<br />
checking whether to build rawshark... yes<br />
checking whether to use libpcap remote capturing feature... no<br />
checking whether to use zlib for gzip compression and decompression... yes<br />
checking zlib.h usability... yes<br />
checking zlib.h presence... yes<br />
checking for zlib.h... yes<br />
checking for inflatePrime... yes<br />
checking for inflatePrime missing when linking with X11... no<br />
checking whether to use libpcre for regular expressions in dfilters... no<br />
checking whether to use liblua for the lua scripting plugin... yes<br />
checking lua.h usability... yes<br />
checking lua.h presence... yes<br />
checking for lua.h... yes<br />
checking lualib.h usability... yes<br />
checking lualib.h presence... yes<br />
checking for lualib.h... yes<br />
checking lauxlib.h usability... yes<br />
checking lauxlib.h presence... yes<br />
checking for lauxlib.h... yes<br />
checking for luaL_register in -llua... yes<br />
checking whether to use libportaudio for the rtp_player... yes<br />
checking portaudio.h usability... no<br />
checking portaudio.h presence... no<br />
checking for portaudio.h... no<br />
libportaudio not found - disabling support for the rtp_player<br />
checking whether to enable ipv6 name resolution if available... yes<br />
checking ipv6 stack type... "unknown, none"<br />
checking for setcap... no<br />
checking whether to install dumpcap with cap_net_admin and cap_net_raw capabilities... no<br />
checking whether to install dumpcap setuid... no<br />
checking for setresuid... no<br />
checking for setresgid... no<br />
checking whether to use the libcap capabilities library... yes<br />
checking for cap_set_flag in -lcap... no<br />
checking direct.h usability... no<br />
checking direct.h presence... no<br />
checking for direct.h... no<br />
checking dirent.h usability... yes<br />
checking dirent.h presence... yes<br />
checking for dirent.h... yes<br />
checking fcntl.h usability... yes<br />
checking fcntl.h presence... yes<br />
checking for fcntl.h... yes<br />
checking grp.h usability... yes<br />
checking grp.h presence... yes<br />
checking for grp.h... yes<br />
checking for inttypes.h... (cached) yes<br />
checking netdb.h usability... yes<br />
checking netdb.h presence... yes<br />
checking for netdb.h... yes<br />
checking pwd.h usability... yes<br />
checking pwd.h presence... yes<br />
checking for pwd.h... yes<br />
checking stdarg.h usability... yes<br />
checking stdarg.h presence... yes<br />
checking for stdarg.h... yes<br />
checking stddef.h usability... yes<br />
checking stddef.h presence... yes<br />
checking for stddef.h... yes<br />
checking for unistd.h... (cached) yes<br />
checking sys/ioctl.h usability... yes<br />
checking sys/ioctl.h presence... yes<br />
checking for sys/ioctl.h... yes<br />
checking sys/param.h usability... yes<br />
checking sys/param.h presence... yes<br />
checking for sys/param.h... yes<br />
checking sys/socket.h usability... yes<br />
checking sys/socket.h presence... yes<br />
checking for sys/socket.h... yes<br />
checking sys/sockio.h usability... yes<br />
checking sys/sockio.h presence... yes<br />
checking for sys/sockio.h... yes<br />
checking for sys/stat.h... (cached) yes<br />
checking sys/time.h usability... yes<br />
checking sys/time.h presence... yes<br />
checking for sys/time.h... yes<br />
checking for sys/types.h... (cached) yes<br />
checking sys/utsname.h usability... yes<br />
checking sys/utsname.h presence... yes<br />
checking for sys/utsname.h... yes<br />
checking sys/wait.h usability... yes<br />
checking sys/wait.h presence... yes<br />
checking for sys/wait.h... yes<br />
checking netinet/in.h usability... yes<br />
checking netinet/in.h presence... yes<br />
checking for netinet/in.h... yes<br />
checking arpa/inet.h usability... yes<br />
checking arpa/inet.h presence... yes<br />
checking for arpa/inet.h... yes<br />
checking arpa/nameser.h usability... yes<br />
checking arpa/nameser.h presence... yes<br />
checking for arpa/nameser.h... yes<br />
checking whether to use SSL library... no<br />
checking whether to use kerberos... yes<br />
checking for krb5-config... /usr/local/bin/krb5-config<br />
checking krb5.h usability... yes<br />
checking krb5.h presence... yes<br />
checking for krb5.h... yes<br />
checking whether the Kerberos library is Heimdal or MIT... MIT<br />
checking whether MIT includes krb5_kt_resolve... no<br />
checking whether MIT includes krb5_kt_resolve (linking with -lresolv)... no<br />
Usable MIT not found - disabling dissection for some kerberos data in packet decoding<br />
checking whether to use the c-ares library if available... yes<br />
checking for ares_init in -lcares... no<br />
checking whether to use the GNU ADNS library if available... yes<br />
checking for adns_init in -ladns... yes<br />
checking whether to use the GeoIP IP address mapping library if available... yes<br />
checking for GeoIP_new in -lGeoIP... yes<br />
checking for tm_zone in struct tm... no<br />
checking for tzname... yes<br />
checking for sa_len in struct sockaddr... no<br />
checking whether byte ordering is bigendian... no<br />
checking whether gcc needs -traditional... no<br />
checking for getopt... yes<br />
checking for strncasecmp... yes<br />
checking for mkstemp... yes<br />
checking for mkdtemp... no<br />
checking for library containing inet_aton... -lnsl<br />
checking for library containing inet_pton... none required<br />
checking for broken inet_pton... ok<br />
checking for library containing inet_ntop... none required<br />
checking for inet_ntop prototype... yes<br />
checking for strptime... yes<br />
checking for getprotobynumber... no<br />
checking for gethostbyname2... no<br />
checking for issetugid... yes<br />
checking for mmap... yes<br />
checking for mprotect... yes<br />
checking for sysconf... yes<br />
checking for strtoll... yes<br />
configure: creating ./config.status<br />
config.status: creating Makefile<br />
config.status: creating doxygen.cfg<br />
config.status: creating asn1/Makefile<br />
config.status: creating asn1/acp133/Makefile<br />
config.status: creating asn1/acse/Makefile<br />
config.status: creating asn1/ansi_map/Makefile<br />
config.status: creating asn1/ansi_tcap/Makefile<br />
config.status: creating asn1/camel/Makefile<br />
config.status: creating asn1/cdt/Makefile<br />
config.status: creating asn1/charging_ase/Makefile<br />
config.status: creating asn1/cmip/Makefile<br />
config.status: creating asn1/cmp/Makefile<br />
config.status: creating asn1/crmf/Makefile<br />
config.status: creating asn1/cms/Makefile<br />
config.status: creating asn1/dap/Makefile<br />
config.status: creating asn1/disp/Makefile<br />
config.status: creating asn1/dop/Makefile<br />
config.status: creating asn1/dsp/Makefile<br />
config.status: creating asn1/ess/Makefile<br />
config.status: creating asn1/ftam/Makefile<br />
config.status: creating asn1/gnm/Makefile<br />
config.status: creating asn1/goose/Makefile<br />
config.status: creating asn1/gprscdr/Makefile<br />
config.status: creating asn1/gsm_map/Makefile<br />
config.status: creating asn1/h225/Makefile<br />
config.status: creating asn1/h235/Makefile<br />
config.status: creating asn1/h245/Makefile<br />
config.status: creating asn1/h248/Makefile<br />
config.status: creating asn1/h282/Makefile<br />
config.status: creating asn1/h283/Makefile<br />
config.status: creating asn1/h323/Makefile<br />
config.status: creating asn1/h450/Makefile<br />
config.status: creating asn1/h450-ros/Makefile<br />
config.status: creating asn1/h460/Makefile<br />
config.status: creating asn1/h501/Makefile<br />
config.status: creating asn1/HI2Operations/Makefile<br />
config.status: creating asn1/hnbap/Makefile<br />
config.status: creating asn1/idmp/Makefile<br />
config.status: creating asn1/inap/Makefile<br />
config.status: creating asn1/kerberos/Makefile<br />
config.status: creating asn1/ldap/Makefile<br />
config.status: creating asn1/logotypecertextn/Makefile<br />
config.status: creating asn1/lte-rrc/Makefile<br />
config.status: creating asn1/mms/Makefile<br />
config.status: creating asn1/mpeg-audio/Makefile<br />
config.status: creating asn1/mpeg-pes/Makefile<br />
config.status: creating asn1/nbap/Makefile<br />
config.status: creating asn1/ns_cert_exts/Makefile<br />
config.status: creating asn1/ocsp/Makefile<br />
config.status: creating asn1/p1/Makefile<br />
config.status: creating asn1/p22/Makefile<br />
config.status: creating asn1/p7/Makefile<br />
config.status: creating asn1/p772/Makefile<br />
config.status: creating asn1/pcap/Makefile<br />
config.status: creating asn1/pkcs1/Makefile<br />
config.status: creating asn1/pkcs12/Makefile<br />
config.status: creating asn1/pkinit/Makefile<br />
config.status: creating asn1/pkixac/Makefile<br />
config.status: creating asn1/pkix1explicit/Makefile<br />
config.status: creating asn1/pkix1implicit/Makefile<br />
config.status: creating asn1/pkixproxy/Makefile<br />
config.status: creating asn1/pkixqualified/Makefile<br />
config.status: creating asn1/pkixtsp/Makefile<br />
config.status: creating asn1/pres/Makefile<br />
config.status: creating asn1/q932/Makefile<br />
config.status: creating asn1/q932-ros/Makefile<br />
config.status: creating asn1/qsig/Makefile<br />
config.status: creating asn1/ranap/Makefile<br />
config.status: creating asn1/rnsap/Makefile<br />
config.status: creating asn1/ros/Makefile<br />
config.status: creating asn1/rrc/Makefile<br />
config.status: creating asn1/rrlp/Makefile<br />
config.status: creating asn1/rtse/Makefile<br />
config.status: creating asn1/rua/Makefile<br />
config.status: creating asn1/s1ap/Makefile<br />
config.status: creating asn1/sabp/Makefile<br />
config.status: creating asn1/smrse/Makefile<br />
config.status: creating asn1/snmp/Makefile<br />
config.status: creating asn1/spnego/Makefile<br />
config.status: creating asn1/sv/Makefile<br />
config.status: creating asn1/t125/Makefile<br />
config.status: creating asn1/t38/Makefile<br />
config.status: creating asn1/tcap/Makefile<br />
config.status: creating asn1/tetra/Makefile<br />
config.status: creating asn1/ulp/Makefile<br />
config.status: creating asn1/wlancertextn/Makefile<br />
config.status: creating asn1/x2ap/Makefile<br />
config.status: creating asn1/x509af/Makefile<br />
config.status: creating asn1/x509ce/Makefile<br />
config.status: creating asn1/x509if/Makefile<br />
config.status: creating asn1/x509sat/Makefile<br />
config.status: creating asn1/x721/Makefile<br />
config.status: creating doc/Makefile<br />
config.status: creating docbook/Makefile<br />
config.status: creating epan/Makefile<br />
config.status: creating epan/crc/Makefile<br />
config.status: creating epan/crypt/Makefile<br />
config.status: creating epan/doxygen.cfg<br />
config.status: creating epan/dfilter/Makefile<br />
config.status: creating epan/dissectors/Makefile<br />
config.status: creating epan/dissectors/dcerpc/Makefile<br />
config.status: creating epan/dissectors/pidl/Makefile<br />
config.status: creating epan/ftypes/Makefile<br />
config.status: creating epan/wslua/Makefile<br />
config.status: creating epan/wspython/Makefile<br />
config.status: creating codecs/Makefile<br />
config.status: creating gtk/Makefile<br />
config.status: creating gtk/doxygen.cfg<br />
config.status: creating help/Makefile<br />
config.status: creating packaging/Makefile<br />
config.status: creating packaging/macosx/Info.plist<br />
config.status: creating packaging/macosx/Makefile<br />
config.status: creating packaging/nsis/Makefile<br />
config.status: creating packaging/rpm/Makefile<br />
config.status: creating packaging/rpm/SPECS/Makefile<br />
config.status: creating packaging/rpm/SPECS/wireshark.spec<br />
config.status: creating packaging/svr4/Makefile<br />
config.status: creating packaging/svr4/checkinstall<br />
config.status: creating packaging/svr4/pkginfo<br />
config.status: creating plugins/Makefile<br />
config.status: creating plugins/asn1/Makefile<br />
config.status: creating plugins/docsis/Makefile<br />
config.status: creating plugins/ethercat/Makefile<br />
config.status: creating plugins/giop/Makefile<br />
config.status: creating plugins/gryphon/Makefile<br />
config.status: creating plugins/interlink/Makefile<br />
config.status: creating plugins/irda/Makefile<br />
config.status: creating plugins/m2m/Makefile<br />
config.status: creating plugins/mate/Makefile<br />
config.status: creating plugins/opcua/Makefile<br />
config.status: creating plugins/profinet/Makefile<br />
config.status: creating plugins/sercosiii/Makefile<br />
config.status: creating plugins/stats_tree/Makefile<br />
config.status: creating plugins/unistim/Makefile<br />
config.status: creating plugins/wimax/Makefile<br />
config.status: creating plugins/wimaxasncp/Makefile<br />
config.status: creating tools/Makefile<br />
config.status: creating tools/idl2wrs.sh<br />
config.status: creating tools/lemon/Makefile<br />
config.status: creating wiretap/Makefile<br />
config.status: creating wsutil/Makefile<br />
config.status: creating config.h<br />
config.status: config.h is unchanged<br />
config.status: executing depfiles commands<br />
config.status: executing libtool commands<br />
<br />
The Wireshark package has been configured with the following options.<br />
Build wireshark : yes<br />
Build tshark : yes<br />
Build capinfos : yes<br />
Build editcap : yes<br />
Build dumpcap : yes<br />
Build mergecap : yes<br />
Build text2pcap : yes<br />
Build idl2wrs : yes<br />
Build randpkt : yes<br />
Build dftest : yes<br />
Build rawshark : yes<br />
<br />
Install dumpcap with capabilities : no<br />
Install dumpcap setuid : no<br />
Use dumpcap group : (none)<br />
Use plugins : yes<br />
Use lua library : yes<br />
Use python binding : no<br />
Build rtp_player : no<br />
Use threads : no<br />
Build profile binaries : no<br />
Use pcap library : yes<br />
Use zlib library : yes<br />
Use pcre library : no (using GRegex instead)<br />
Use kerberos library : no<br />
Use c-ares library : no<br />
Use GNU ADNS library : yes<br />
Use SMI MIB library : no<br />
Use GNU crypto library : yes<br />
Use SSL crypto library : no<br />
Use IPv6 name resolution : no<br />
Use gnutls library : yes<br />
Use POSIX capabilities library : no<br />
Use GeoIP library : yes<br />
johndeere {root}# make<br />
make: Fatal error in reader: Makefile, line 4159: Unexpected end of line seen<br />
johndeere {root}#<br />
<br />
script done on Mon May 07 16:38:52 2012<br />
<br />
</p><p><br />
Here is the line in the Makefile it fails on. I can provide more info, but this was getting to be a long message anyway..<br />
<br />
dc_install_base=<code>$(am__cd) $(distdir)/_inst &amp;&amp; pwd | sed -e 's,^[^:\\/]:[\\/],/,'</code><br />
</p><p>Any thoughts or ideas??<br />
</p><p>Thanks! Bryan</p></div><div id="question-tags" class="tags-container tags">compile solaris makefile</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '12, 13:53</strong></p><img src="https://secure.gravatar.com/avatar/597eef99fea106df3d9a101ad3ba8b02?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johndeere&#39;s gravatar image" /><p>johndeere<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johndeere has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-10749" class="comments-container"><span id="10752"></span><div id="comment-10752" class="comment"><div id="post-10752-score" class="comment-score">1</div><div class="comment-text"><p>sounds like a problem with Solaris 'make'. Try to use the latest available GNU make.</p><p>Regards<br />
Kurt</p></div><div id="comment-10752-info" class="comment-info"><span class="comment-age">(07 May '12, 15:40)</span> Kurt Knochner ♦</div></div><span id="10776"></span><div id="comment-10776" class="comment"><div id="post-10776-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt. Obvious answer.. I thought I'd tried that one but I guess that's what happens when you've been compiling all day and the brain is fried.</p></div><div id="comment-10776-info" class="comment-info"><span class="comment-age">(08 May '12, 04:39)</span> johndeere</div></div></div><div id="comment-tools-10749" class="comment-tools"></div><div class="clear"></div><div id="comment-10749-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10757"></span>

<div id="answer-container-10757" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10757-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As @Kurt says, you have to use GNU make. You might want to look at the "configure" and "compile" steps in the <a href="http://buildbot.wireshark.org/trunk/waterfall?show=Solaris-10-SPARC">Solaris buildbot</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '12, 16:01</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span> </br></br></p></div></div><div id="comments-container-10757" class="comments-container"><span id="10777"></span><div id="comment-10777" class="comment"><div id="post-10777-score" class="comment-score"></div><div class="comment-text"><p>Thanks Gerald! Obvious answer.. I thought I'd tried that one but I guess that's what happens when you've been compiling all day and the brain is fried.</p><p>I'll take a look at the Solaris buildbot as well.</p></div><div id="comment-10777-info" class="comment-info"><span class="comment-age">(08 May '12, 04:39)</span> johndeere</div></div></div><div id="comment-tools-10757" class="comment-tools"></div><div class="clear"></div><div id="comment-10757-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

